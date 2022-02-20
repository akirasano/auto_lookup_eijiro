from typing import Dict, Optional

import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                             QProgressDialog, QPushButton, QTextEdit,
                             QVBoxLayout, QWidget)


class Dialog(QDialog):

    pushed_add = QtCore.pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle("Look up the words")
        self.vb_layout = QVBoxLayout()

        self.text_edit = QTextEdit()

        self.btn_layout = QHBoxLayout()
        self.add_button = QPushButton("Lookup & add")
        self.add_button.clicked.connect(self.add)

        self.cancel_button = QPushButton("Cancel")
        self.btn_layout.addWidget(self.add_button)
        self.btn_layout.addWidget(self.cancel_button)

        self.vb_layout.addWidget(self.text_edit)
        self.vb_layout.addLayout(self.btn_layout)

        self.setLayout(self.vb_layout)

    def add(self):
        self.pushed_add.emit(self.text_edit.toPlainText())
        self.close()

    def cancel(self):
        self.close()


if __name__ == "__main__":
    import os
    import sys

    dirname = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dirname, "Qt5", "plugins", "platforms")
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path

    app = QApplication(sys.argv)
    gallery = Dialog()
    gallery.show()
    sys.exit(app.exec_())
