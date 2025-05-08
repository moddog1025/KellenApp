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
            background-color: #FFFFFF;
        }
        QPushButton {
            background: none;
            border: none;
            font: 14px "Segoe UI";
            color: #0078D4;
        }
        QPushButton:hover {
            text-decoration: underline;
        }
        QLabel {
            font: 14px "Segoe UI";
            color: #333333;
        }
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 8, 16, 8)
        layout.setSpacing(8)

        if back:
            self.back_btn = QPushButton("← Back")
            self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            layout.addWidget(self.back_btn)
        else:
            layout.addSpacing(80)

        if title:
            lbl = QLabel(title)
            lbl.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(lbl, stretch=1)

        layout.addStretch()
