from PyQt5 import QtCore, QtGui, QtWidgets


class WindowForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Карты')

        MainWindow.pixmap = QtGui.QPixmap()
        MainWindow.pixmap.loadFromData(MainWindow.map)
        MainWindow.image = QtWidgets.QLabel(MainWindow)
        MainWindow.image.move(0, 0)
        MainWindow.image.resize(600, 450)
        MainWindow.image.setPixmap(MainWindow.pixmap)




