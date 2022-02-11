from data.ui.mainForm import *
from scripts.functions import *
from scripts.params import *

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QByteArray


class Window(QWidget, WindowForm):
    def __init__(self):
        super().__init__()

        self.setFixedSize(*SCREEN_SIZE)
        self.object_coords = [37.530887, 55.70311]
        self.cur_coords = self.object_coords
        self.zoom = 17
        self.points = None
        self.view = 'map'
        self.postcode = False
        self.setupUi(self)
        self.view_show.clicked.connect(self.negative_views)
        self.view_map.clicked.connect(self.set_view_map)
        self.view_sat.clicked.connect(self.set_view_sat)
        self.view_satskl.clicked.connect(self.set_view_satskl)
        self.searchButton.clicked.connect(self.search)
        self.clearButton.clicked.connect(self.searchLine.clear)
        self.resetButton.clicked.connect(self.reset)
        self.postcodeCheck.stateChanged.connect(self.postcodeState)

        self.updateMap()
        self.set_text_address()

    def postcodeState(self, state):
        self.postcode = True if state == Qt.Checked else False
        self.set_text_address()

    def reset(self):
        self.points = None
        self.searchLine.clear()
        self.text_address.setText('')
        self.updateMap()

    def search(self):
        s = self.searchLine.text()
        if s:
            coord = get_coords(s)
            if coord:
                self.object_coords = [float(i) for i in coord.split(',')]
                self.cur_coords = self.object_coords
                self.points = [coord + ',pm2rdm']
                self.resetButton.show()
                self.set_text_address()
                self.updateMap()
            else:
                self.text_address.setText('Ошибка выполнения запроса')
                self.points = None
                self.updateMap()

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.pos().x() < 650:
            if e.button() == Qt.LeftButton:
                x = self.cur_coords[0] + 0.00694 * 2 ** (17 - self.zoom) * (e.pos().x() - 325) / 650
                y = self.cur_coords[1] - 0.00265 * 2 ** (17 - self.zoom) * (e.pos().y() - 225) / 450
                self.object_coords = [x, y]
                self.cur_coords = self.object_coords
                self.points = [f"{x},{y}" + ',pm2rdm']
                self.resetButton.show()
                self.set_text_address()
                self.updateMap()
            elif e.button() == Qt.RightButton:
                x = self.cur_coords[0] + 0.00694 * 2 ** (17 - self.zoom) * (e.pos().x() - 325) / 650
                y = self.cur_coords[1] - 0.00265 * 2 ** (17 - self.zoom) * (e.pos().y() - 225) / 450
                org, res = get_organization(f'{str(x)},{str(y)}')
                if res is not None:
                    res = list(map(float, res.split(',')))
                    s = lonlat_distance(res, [x, y])
                    if s > 50:
                        return self.reset()
                    self.object_coords = res
                    self.cur_coords = self.object_coords
                    self.points = [f"{res[0]},{res[1]},pm2rdm"]
                    self.resetButton.show()
                    self.set_text_address(org)
                    self.updateMap()
                else:
                    self.reset()

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
        image = get_image(' '.join(map(str, self.cur_coords)), self.zoom, self.view, points=self.points)
        if image:
            map_img = QByteArray(image)
            self.pixmap.loadFromData(map_img)
            self.image.setPixmap(self.pixmap)
        else:
            self.text_address.setText('Ошибка выполнения запроса')
            self.points.clear()
            self.updateMap()

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

    def set_text_address(self, message=None):
        if message is not None:
            self.text_address.setText(message)
        else:
            self.text_address.setText(get_address(' '.join(map(str, self.cur_coords)), self.postcode))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
