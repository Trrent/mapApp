from PyQt5 import QtCore, QtGui, QtWidgets


class WindowForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Карты')
        MainWindow.setFixedSize(650, 450)

        MainWindow.pixmap = QtGui.QPixmap()
        MainWindow.image = QtWidgets.QLabel(MainWindow)
        MainWindow.image.move(0, 0)
        MainWindow.image.resize(650, 450)

        # Вид карты (Схема/Спутник/Гибрид)
        # Кнопка "Вид"
        MainWindow.view_show = QtWidgets.QPushButton(MainWindow)
        MainWindow.view_show.move(5, 415)
        MainWindow.view_show.resize(50, 30)
        MainWindow.view_show.setText('Вид')
        MainWindow.view_show.setStyleSheet('background-color: #ffcc00')
        MainWindow.view_show.setFocusPolicy(QtCore.Qt.NoFocus)
        # Кнопка "Схема"
        MainWindow.view_map = QtWidgets.QPushButton(MainWindow)
        MainWindow.view_map.move(5, 380)
        MainWindow.view_map.resize(100, 30)
        MainWindow.view_map.setText('Схема')
        MainWindow.view_map.setStyleSheet('background-color: #ffcc00')
        MainWindow.view_map.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.view_map.hide()
        # Кнопка "Спутник"
        MainWindow.view_sat = QtWidgets.QPushButton(MainWindow)
        MainWindow.view_sat.move(5, 348)
        MainWindow.view_sat.resize(100, 30)
        MainWindow.view_sat.setText('Спутник')
        MainWindow.view_sat.setStyleSheet('background-color: #ffcc00')
        MainWindow.view_sat.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.view_sat.hide()
        # Кнопка "Гибрид"
        MainWindow.view_satskl = QtWidgets.QPushButton(MainWindow)
        MainWindow.view_satskl.move(5, 316)
        MainWindow.view_satskl.resize(100, 30)
        MainWindow.view_satskl.setText('Гибрид')
        MainWindow.view_satskl.setStyleSheet('background-color: #ffcc00')
        MainWindow.view_satskl.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.view_satskl.hide()
