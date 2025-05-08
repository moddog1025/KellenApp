# src/app/posts/text_post.py

from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import pyqtSignal, Qt
from app.gui.widgets import CardWidget

class TextPostWidget(CardWidget):
    clicked = pyqtSignal()

    def __init__(self, text: str, border_color: str = "#FFFFFF"):
        super().__init__(border_color=border_color)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)
        new_color = lighten_color(border_color, 0.4)

        lbl = QLabel(text)
        lbl.setWordWrap(True)
        lbl.setFont(QFont("Segoe UI", 12))
        lbl.setStyleSheet("background-color: {}; color: black;".format(border_color))

        layout.addWidget(lbl)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(event)

def lighten_color(hex_color: str, factor: float = 0.4) -> QColor:
    """
    Lighten a hex color by mixing it with white.
    factor=0.0 → original color; factor=1.0 → pure white.
    """
    c = hex_color.lstrip('#')
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    r = min(255, int(r + (255 - r) * factor))
    g = min(255, int(g + (255 - g) * factor))
    b = min(255, int(b + (255 - b) * factor))
    return QColor(r, g, b)
