# src/app/posts/image_post.py

from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, Qt
from app.gui.widgets import CardWidget

class ImagePostWidget(CardWidget):
    clicked = pyqtSignal()

    def __init__(self, image_path: str, border_color: str = "#FFFFFF"):
        super().__init__(border_color=border_color)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        pix = QPixmap(image_path)
        pix = pix.scaledToWidth(360, Qt.TransformationMode.SmoothTransformation)

        img_lbl = QLabel()
        img_lbl.setPixmap(pix)
        img_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(img_lbl)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(event)
