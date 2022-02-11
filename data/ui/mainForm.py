from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

imagesPath = Path(Path(__file__).parent.parent, 'image')


class WindowForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('Карты')
        MainWindow.setFixedSize(900, 450)

        MainWindow.pixmap = QtGui.QPixmap()
        MainWindow.image = QtWidgets.QLabel(MainWindow)
        MainWindow.image.move(0, 0)
        MainWindow.image.resize(650, 450)

        MainWindow.searchLine = ClickableLine(MainWindow)
        MainWindow.searchLine.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.searchLine.setFont(font)
        MainWindow.searchLine.setMaxLength(60)
        MainWindow.searchLine.move(25, 10)
        MainWindow.searchLine.resize(500, 30)

        MainWindow.searchButton = QtWidgets.QPushButton('Поиск', MainWindow)
        MainWindow.searchButton.setGeometry(525, 10, 60, 31)
        MainWindow.searchButton.setStyleSheet('background-color: #ffcc00')

        MainWindow.clearButton = QtWidgets.QPushButton('Стереть', MainWindow)
        MainWindow.clearButton.setGeometry(585, 10, 60, 31)
        MainWindow.clearButton.setStyleSheet('background-color: #ffcc00')

        MainWindow.resetButton = QtWidgets.QPushButton('Сброс', MainWindow)
        MainWindow.resetButton.setGeometry(585, 41, 60, 31)
        MainWindow.resetButton.setStyleSheet('background-color: #ffcc00')
        MainWindow.resetButton.hide()

        MainWindow.postcodeCheck = QtWidgets.QCheckBox('Выводить индекс', MainWindow)
        MainWindow.postcodeCheck.move(660, 415)

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

        # Поле для адресов
        # Label для надписи "Адрес:"
        MainWindow.label_address = QtWidgets.QLabel(MainWindow)
        MainWindow.label_address.move(660, 10)
        MainWindow.label_address.resize(240, 30)
        MainWindow.label_address.setText('Адрес:')
        # Поле адреса
        MainWindow.text_address = QtWidgets.QTextEdit(MainWindow)
        MainWindow.text_address.setReadOnly(True)
        MainWindow.text_address.move(655, 40)
        MainWindow.text_address.resize(240, 90)
        MainWindow.text_address.setStyleSheet('background-color: #ffffff')


class ClickableLine(QtWidgets.QLineEdit):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(ClickableLine, self).__init__(parent)
        self.parent = parent

    def mouseReleaseEvent(self, e):
        if self.isReadOnly():
            self.setReadOnly(False)
        else:
            self.setReadOnly(True)
        self.clicked.emit()

    def keyPressEvent(self, event):
        if self.isReadOnly():
            self.parent.keyPressEvent(event)
        else:
            super(ClickableLine, self).keyPressEvent(event)
