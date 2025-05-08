# src/app/gui/comment_page.py

import random
import string
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtCore import pyqtSignal
from app.gui.tool_bar import ToolBar
from app.posts.comment import CommentWidget
from random import randint
from app.gui.main_feed import _COMMENT_SAMPLES

# alternating border‑colors for comments
_COMMENT_COLORS = ["#8EBDC4", "#C4F0F0"]

class CommentPageWidget(QWidget):
    back_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #92DCE5;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = ToolBar(self, title="Comments", back=True)
        toolbar.back_btn.clicked.connect(self.back_clicked.emit)
        layout.addWidget(toolbar)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        layout.addWidget(scroll)

        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(12)

        for i in range(randint(0, 8)):
            user = "@" + "".join(random.choices(string.ascii_lowercase, k=6))
            text = random.choice(_COMMENT_SAMPLES)
            color = _COMMENT_COLORS[i % len(_COMMENT_COLORS)]
            comment = CommentWidget(text, user, border_color=color)
            vbox.addWidget(comment)

        vbox.addStretch()
        scroll.setWidget(container)
