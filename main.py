from data.ui.mainForm import *
from scripts.functions import *
from scripts.params import *

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QByteArray


class Window(QWidget, WindowForm):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, *SCREEN_SIZE)
        self.object_coords = [37.530887, 55.70311]
        self.cur_coords = self.object_coords
        self.zoom = 17
        self.view = 'map'
        self.setupUi(self)
        self.view_show.clicked.connect(self.negative_views)
        self.view_map.clicked.connect(self.set_view_map)
        self.view_sat.clicked.connect(self.set_view_sat)
        self.view_satskl.clicked.connect(self.set_view_satskl)
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
        map_img = QByteArray(get_image(' '.join(map(str, self.cur_coords)), self.zoom, self.view))
        self.pixmap.loadFromData(map_img)
        self.image.setPixmap(self.pixmap)

    def negative_views(self):
        if self.view_map.isHidden():
            self.view_map.show()
            self.view_sat.show()
            self.view_satskl.show()
        else:
            self.view_map.hide()
            self.view_sat.hide()
            self.view_satskl.hide()

    def set_view_map(self):
        self.view = 'map'
        self.updateMap()
        self.negative_views()

    def set_view_sat(self):
        self.view = 'sat'
        self.updateMap()
        self.negative_views()

    def set_view_satskl(self):
        self.view = 'sat,skl'
        self.updateMap()
        self.negative_views()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

