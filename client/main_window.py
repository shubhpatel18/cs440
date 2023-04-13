#!/usr/bin/env python3.8

import sys
import signal
from pathlib import Path

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, title: str="Team Tau Fantasy Football", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # icon_path = Path(__file__).parent.resolve / "filepath/filename"
        # self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle(title)

        self.layout = QVBoxLayout()

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.shortcut_fullscreen = QShortcut(QKeySequence('F11'), self)
        self.shortcut_fullscreen.activated.connect(self.toggle_fullscreen)

        self.shortcut_exit_fullscreen = QShortcut(QKeySequence('Escape'), self)
        self.shortcut_exit_fullscreen.activated.connect(self.exit_fullscreen)

        self.shortcut_quit = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_quit.activated.connect(self.sigHandler)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def exit_fullscreen(self):
        self.showNormal()

    def sigHandler(*args):
        QApplication.quit()

class AppRunner():
    def __init__(self, WindowType: QMainWindow):
        self.WindowType = WindowType

    def start(self):
        app = QApplication(sys.argv)

        window = self.WindowType()
        window.show()

        signal.signal(signal.SIGINT, window.sigHandler)

        timer = QTimer()
        timer.start(500)
        timer.timeout.connect(lambda: None)

        sys.exit(app.exec_())

if __name__ == '__main__':
    app = AppRunner(MainWindow)
    app.start()