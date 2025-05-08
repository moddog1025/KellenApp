# src/app/gui/tool_bar.py

from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class ToolBar(QFrame):
    def __init__(self, parent=None, title: str = "", back: bool = False):
        super().__init__(parent)
        self.setObjectName("toolbar")
        self.setStyleSheet("""
        QFrame#toolbar {
            background: transparent;
        }
        QPushButton {
            background: none;
            border: none;
            font: 14px "Segoe UI";
            color: #333333;
        }
        QPushButton:hover {
            text-decoration: underline;
        }
        QLabel {
            font: 16px "Segoe UI";
            color: #222222;
        }
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        if back:
            self.back_btn = QPushButton("← Back")
            self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            layout.addWidget(self.back_btn)

        layout.addStretch()
        if title:
            lbl = QLabel(title)
            lbl.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(lbl)
        layout.addStretch()
