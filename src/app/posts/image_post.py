# src/app/posts/image_post.py

from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal, Qt
from app.gui.widgets import CardWidget

class ImagePostWidget(CardWidget):
    clicked = pyqtSignal()

    def __init__(self, image_path: str):
        super().__init__()
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaledToWidth(360, Qt.TransformationMode.SmoothTransformation)
        img_label = QLabel()
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(img_label)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(event)
