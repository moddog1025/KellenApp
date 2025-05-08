# src/app/posts/text_post.py

from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal, Qt
from app.gui.widgets import CardWidget

class TextPostWidget(CardWidget):
    clicked = pyqtSignal()

    def __init__(self, text: str):
        super().__init__()
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        label = QLabel(text)
        label.setWordWrap(True)
        label.setFont(QFont("Segoe UI", 12))
        layout.addWidget(label)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(event)
