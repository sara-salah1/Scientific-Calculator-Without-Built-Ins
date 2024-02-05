from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QListWidget, QVBoxLayout, QLabel


class HistoryDialog(QDialog):
    def __init__(self, history):
        super().__init__()

        self.setWindowTitle("History")
        self.setWindowIcon(QIcon("D:/ITGate(AI Diploma)/Projects/Scientific Calculator/history_tracking.png"))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setGeometry(200, 200, 410, 200)

        self.history = history

        self.init_ui()

    def init_ui(self):
        self.create_widgets()
        self.create_layout()
        self.style()
        self.center_on_screen()

    def create_widgets(self):
        self.history_list = QListWidget()
        self.history_list.addItems(self.history)

        self.title_label = QLabel("History Tracking")

    def style(self):
        self.title_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: black;")

        font = QFont()
        font.setBold(True)
        for i in range(self.history_list.count()):
            item = self.history_list.item(i)
            item.setFont(font)

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.history_list)
        self.setLayout(layout)

    def center_on_screen(self):
        screen_geometry = self.screen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())
