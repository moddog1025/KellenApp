import os
import shutil
from pathlib import Path
from datetime import datetime
import subprocess
import sys

def generate_filetree_lines(root_dir: Path, hidden_dirs: set[str] | None = None) -> list[str]:
    if hidden_dirs is None:
        hidden_dirs = {'.venv', '__pycache__'}

    def walk(directory: Path, prefix: str = "") -> list[str]:
        entries = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        lines: list[str] = []
        for idx, entry in enumerate(entries):
            connector = '└──' if idx == len(entries) - 1 else '├──'
            line = f"{prefix}{connector} {entry.name}"
            lines.append(line)

            if entry.is_dir() and entry.name not in hidden_dirs:
                extension = '    ' if idx == len(entries) - 1 else '│   '
                lines.extend(walk(entry, prefix + extension))
        return lines

    tree = [root_dir.name]
    tree.extend(walk(root_dir))
    return tree

def compile_mega_file(output_file: Path, project_root: Path, hidden_dirs: set[str] | None = None) -> None:
    if hidden_dirs is None:
        hidden_dirs = {'.venv', '__pycache__'}

    tree_lines = generate_filetree_lines(project_root, hidden_dirs)

    with output_file.open('w', encoding='utf-8') as out:
        out.write(f"# Project Filetree: {project_root.name}\n\n")
        out.write("\n".join(tree_lines))
        out.write("\n\n")

        src_dir = project_root / 'src'
        if not src_dir.exists():
            out.write("# No 'src' directory found.\n")
            return

        for py_file in sorted(src_dir.rglob('*.py')):
            if any(part in hidden_dirs for part in py_file.parts):
                continue
            if py_file.name == '__init__.py':
                continue

            rel_path = py_file.relative_to(project_root)
            out.write(f"## ===== {rel_path} =====\n\n")

            try:
                content = py_file.read_text(encoding='utf-8')
            except Exception as e:
                out.write(f"# ERROR reading file: {e}\n\n")
                continue

            out.write(content)
            out.write("\n\n")

def copy_to_clipboard(file_path: Path):
    try:
        if sys.platform == 'win32':
            subprocess.run(['powershell', '-Command', f'Get-Content -Raw "{file_path}" | Set-Clipboard'], check=True)
        elif sys.platform == 'darwin':
            subprocess.run(['pbcopy'], input=file_path.read_bytes(), check=True)
        else:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=file_path.read_bytes(), check=True)
        print(f"Copied {file_path.name} to clipboard.")
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

def main():
    utils_dir = Path(__file__).resolve().parent
    project_root = utils_dir.parent

    # Get the user's Downloads folder
    downloads_dir = Path(os.path.expanduser('~/Downloads'))
    downloads_dir.mkdir(exist_ok=True)

    mega_file = downloads_dir / f"project_breakdown.txt"

    compile_mega_file(mega_file, project_root)
    copy_to_clipboard(mega_file)
    print(f"Mega file generated and copied to clipboard: {mega_file}")


if __name__ == '__main__':
    main()
 