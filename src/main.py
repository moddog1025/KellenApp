import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from app.gui.main_feed import MainFeedWidget
from app.gui.comment_page import CommentPageWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mock Social App")
        self.stack = QStackedWidget()
        self.feed = MainFeedWidget()
        self.comments = CommentPageWidget()
        self.stack.addWidget(self.feed)
        self.stack.addWidget(self.comments)
        self.setCentralWidget(self.stack)
        self.feed.post_clicked.connect(self.show_comments)
        self.comments.back_clicked.connect(self.show_feed)

    def show_comments(self):
        self.stack.setCurrentWidget(self.comments)

    def show_feed(self):
        self.stack.setCurrentWidget(self.feed)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(390, 844)
    window.show()
    sys.exit(app.exec())
