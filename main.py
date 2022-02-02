from data.ui.mainForm import *
from scripts.functions import *
from scripts.params import *

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QByteArray


class Window(QWidget, WindowForm):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, *SCREEN_SIZE)
        self.map = QByteArray(get_image('37.530887 55.70311', 17))
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

