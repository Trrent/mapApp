import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QAbstractButton, QApplication, QWidget, QHBoxLayout
from pathlib import Path


imagesPath = Path(Path(__file__).parent.parent, 'image')


class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()
    # def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
    #     super(PicButton, self).__init__(parent)
    #     self.pixmap = pixmap
    #     self.pixmap_hover = pixmap_hover
    #     self.pixmap_pressed = pixmap_pressed
    #
    #     self.pressed.connect(self.update)
    #     self.released.connect(self.update)
    #
    # def paintEvent(self, event):
    #     pix = self.pixmap_hover if self.underMouse() else self.pixmap
    #     if self.isDown():
    #         pix = self.pixmap_pressed
    #
    #     painter = QPainter(self)
    #     painter.drawPixmap(event.rect(), pix)
    #
    # def enterEvent(self, event):
    #     self.update()
    #
    # def leaveEvent(self, event):
    #     self.update()
    #
    # def sizeHint(self):
    #     return QSize(200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QHBoxLayout(window)
    image = Path(imagesPath, "search.png")

    button = PicButton(QPixmap(image))
    layout.addWidget(button)

    window.show()
    sys.exit(app.exec_())
