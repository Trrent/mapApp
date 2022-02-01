import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QByteArray
from .functions import *
from .params import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.map = QByteArray(get_image('37.530887 55.70311'))
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 250, *SCREEN_SIZE)
        self.setWindowTitle('Карты')

        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.map)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)




