# src/app/gui/comment_page.py

import random
import string
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame
from PyQt6.QtCore import pyqtSignal
from app.gui.tool_bar import ToolBar
from app.posts.comment import CommentWidget

class CommentPageWidget(QWidget):
    back_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Top bar with Back button
        toolbar = ToolBar(self, title="Comments", back=True)
        toolbar.back_btn.clicked.connect(self.back_clicked.emit)
        layout.addWidget(toolbar)

        # Scrollable comments list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        layout.addWidget(scroll)

        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(12)

        # Random mock comments
        num_comments = random.randint(1, 5)
        for i in range(num_comments):
            uname = "@" + "".join(random.choices(string.ascii_lowercase, k=6))
            text = f"Mock comment {i+1}: Lorem ipsum dolor sit amet."
            comment = CommentWidget(text, uname)
            vbox.addWidget(comment)

        vbox.addStretch()
        scroll.setWidget(container)
