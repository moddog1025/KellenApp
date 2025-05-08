# src/app/posts/comment.py

from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from app.gui.widgets import CardWidget

class CommentWidget(CardWidget):
    def __init__(self, text: str, username: str):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(4)

        user_lbl = QLabel(username)
        user_lbl.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        layout.addWidget(user_lbl)

        text_lbl = QLabel(text)
        text_lbl.setWordWrap(True)
        text_lbl.setFont(QFont("Segoe UI", 11))
        layout.addWidget(text_lbl)
