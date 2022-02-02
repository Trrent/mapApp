from data.ui.mainForm import *
from scripts.functions import *
from scripts.params import *

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QByteArray


class Window(QWidget, WindowForm):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, *SCREEN_SIZE)
        self.coords = [37.530887, 55.70311]
        self.setupUi(self)
        self.updateMap()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.coords[1] += 0.00266
        elif event.key() == Qt.Key_Down:
            self.coords[1] -= 0.00266
        elif event.key() == Qt.Key_Right:
            self.coords[0] += 0.00693
        elif event.key() == Qt.Key_Left:
            self.coords[0] -= 0.00693

        self.updateMap()

    def updateMap(self):
        map_img = QByteArray(get_image(' '.join(map(str, self.coords)), 17))
        self.pixmap.loadFromData(map_img)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

