import random
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, \
    QFileDialog

import prompts


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.word_count = QLabel("Word Count: 0")
        self.save = QPushButton("Save")
        self.text_box = QTextEdit()
        self.prompt = QLabel("Prompt: Press \"Reload\" for a prompt!")
        self.reload = QPushButton("Reload Prompt")

        self.setWindowTitle("PromptGenerator")
        self.setWindowIcon(QIcon("toledoprayer.jpg"))
        self.setGeometry(300, 300, 500, 500)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.prompt)
        top_layout.addWidget(self.reload)

        self.text_box.setPlaceholderText("Start writing...")

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.save)
        bottom_layout.addWidget(self.word_count)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.text_box)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.text_box.textChanged.connect(self.update_word_count)
        self.save.clicked.connect(self.save_text)
        self.reload.clicked.connect(self.update_prompt)

    def update_word_count(self):
        text = self.text_box.toPlainText()
        words = text.split()
        self.word_count.setText(f"Word Count: {len(words)}")

    def update_prompt(self):
        promptList = prompts.prompts
        self.prompt.setText(f"Prompt: {random.choice(promptList)}")


    def save_text(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.text_box.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())