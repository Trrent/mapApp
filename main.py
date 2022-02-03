from data.ui.mainForm import *
from scripts.functions import *
from scripts.params import *

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QByteArray


class Window(QWidget, WindowForm):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, *SCREEN_SIZE)
        self.object_coords = [37.530887, 55.70311]  # Координаты текущего объекта
        self.cur_coords = self.object_coords  # Текущие координаты
        self.zoom = 17
        self.setupUi(self)
        self.updateMap()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.cur_coords[1] = check_coordinates(self.cur_coords[1], 0.00266 * 2 ** (17 - self.zoom), 'y')
        if event.key() == Qt.Key_Down:
            self.cur_coords[1] = check_coordinates(self.cur_coords[1], -0.00266 * 2 ** (17 - self.zoom), 'y')
        if event.key() == Qt.Key_Right:
            self.cur_coords[0] = check_coordinates(self.cur_coords[0], 0.00693 * 2 ** (17 - self.zoom), 'x')
        if event.key() == Qt.Key_Left:
            self.cur_coords[0] = check_coordinates(self.cur_coords[0], -0.00693 * 2 ** (17 - self.zoom), 'x')
        if event.key() == Qt.Key_PageUp and self.zoom < 17:
            self.zoom += 1
            if self.zoom == 2:
                self.cur_coords = self.object_coords
        if event.key() == Qt.Key_PageDown and self.zoom > 1:
            self.zoom -= 1
            if self.zoom == 1:
                self.cur_coords = [0.0, 0.0]

        self.updateMap()

    def updateMap(self):
        map_img = QByteArray(get_image(' '.join(map(str, self.cur_coords)), self.zoom))
        self.pixmap.loadFromData(map_img)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

