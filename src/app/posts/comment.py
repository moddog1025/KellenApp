# src/app/posts/comment.py

from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from app.gui.widgets import CardWidget

class CommentWidget(CardWidget):
    def __init__(self, text: str, username: str, border_color: str = "#FFFFFF"):
        """
        :param text: The comment body.
        :param username: The commenter’s handle (e.g. "@user123").
        :param border_color: Hex code for the bubble border; interior is auto‐lightened.
        """
        # Pass border_color into the base CardWidget, with a slightly smaller radius
        super().__init__(border_color=border_color, radius=10)

        # Build out the comment layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        # Username label
        user_lbl = QLabel(username)
        user_lbl.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        layout.addWidget(user_lbl)

        # Comment text
        txt_lbl = QLabel(text)
        txt_lbl.setWordWrap(True)
        txt_lbl.setFont(QFont("Segoe UI", 10))
        layout.addWidget(txt_lbl)
