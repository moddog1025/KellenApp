# src/app/gui/widgets.py

from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt

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

class CardWidget(QFrame):
    def __init__(self, border_color: str = "#FFFFFF", radius: int = 12, parent=None):
        super().__init__(parent)

        # store colours & geometry
        self._border_color   = QColor(border_color)
        self._interior_color = lighten_color(border_color, 0.4)
        self._radius         = radius
        self._border_width   = 4

        # allow the shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 3)
        shadow.setColor(Qt.GlobalColor.black)
        self.setGraphicsEffect(shadow)

        # remove any stylesheet‐driven backgrounds
        self.setStyleSheet("")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 0) fill the entire widget rect with the interior color
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._interior_color)
        painter.drawRect(self.rect())

        # 1) draw the rounded interior for crisp, antialiased edges
        painter.drawRoundedRect(self.rect(), self._radius, self._radius)

        # 2) draw the border on top
        pen = QPen(self._border_color, self._border_width)
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        half = self._border_width // 2
        border_rect = self.rect().adjusted(half, half, -half, -half)
        painter.drawRoundedRect(border_rect, self._radius, self._radius)
