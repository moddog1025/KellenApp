# src/app/gui/main_feed.py

import random
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame
from PyQt6.QtCore import pyqtSignal
from app.posts.image_post import ImagePostWidget
from app.posts.text_post import TextPostWidget
from app.gui.tool_bar import ToolBar

_TEXT_SAMPLES = [
    "Just realized I’ve been microwaving my phone charger for 30 seconds every day… should I be worried?",
    "My dog just judged me for eating cereal at 2am. I think he’s a monster.",
    "If you can’t handle me at my worst, you don’t deserve me at my Uber Eats.",
    "Why does my cat always stare at me like I owe her money?",
    "I accidentally texted my boss “I love you” instead of “I’ll see you tomorrow.” Wish me luck.",
    "Someone just said “bless you” to me after I sneezed. I’m on the bus. That’s creepy.",
    "You ever think about how birds must see us stuffing our faces with pizza and judging the whole species?",
    "My plants are dying because I’m too busy arguing with strangers online. Plot twist: I’m the plant killer.",
    "Saw a guy wearing socks with sandals. Called 911. They agreed it was an emergency.",
    "If pizza is a vegetable, then I’m basically a farmer."
]

class MainFeedWidget(QWidget):
    post_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        # Light gray background behind cards
        self.setStyleSheet("background-color: #F0F0F0;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # App title bar
        toolbar = ToolBar(self, title="Mock Social App")
        layout.addWidget(toolbar)

        # Scrollable feed
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        layout.addWidget(scroll)

        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(16)

        assets_dir = Path(__file__).resolve().parents[3] / "assets"

        for _ in range(15):
            if random.choice([True, False]):
                idx = random.randint(1, 9)
                post = ImagePostWidget(str(assets_dir / f"image_{idx}.jpg"))
            else:
                post = TextPostWidget(random.choice(_TEXT_SAMPLES))
            post.clicked.connect(self.on_post_clicked)
            vbox.addWidget(post)

        vbox.addStretch()
        scroll.setWidget(container)

    def on_post_clicked(self):
        self.post_clicked.emit()
