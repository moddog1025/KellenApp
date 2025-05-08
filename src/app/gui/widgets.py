# src/app/gui/widgets.py

from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt

class CardWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        # White background, rounded corners
        self.setStyleSheet("""
        QFrame#card {
            background-color: #FFFFFF;
            border-radius: 8px;
        }
        """)
        # Subtle drop shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(8)
        shadow.setOffset(0, 2)
        shadow.setColor(Qt.GlobalColor.black)
        self.setGraphicsEffect(shadow)
