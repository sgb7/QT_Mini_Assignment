import sys
from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton
from PySide2.QtCore import QFile, QObject

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):

        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        #always remember to close files
        ui_file.close()

        #add event listener to the 7 button
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        sevenButton.clicked.connect(self.seven_button_clicked)

        eightButton = self.window.findChild(QPushButton, 'eightButton')
        eightButton.clicked.connect(self.eight_button_clicked)

        nineButton = self.window.findChild(QPushButton, 'nineButton')
        nineButton.clicked.connect(self.nine_button_clicked)

        fourButton = self.window.findChild(QPushButton, 'fourButton')
        fourButton.clicked.connect(self.four_button_clicked)

        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        fiveButton.clicked.connect(self.five_button_clicked)

        sixButton = self.window.findChild(QPushButton, 'sixButton')
        sixButton.clicked.connect(self.six_button_clicked)

        oneButton = self.window.findChild(QPushButton, 'oneButton')
        oneButton.clicked.connect(self.one_button_clicked)

        twoButton = self.window.findChild(QPushButton, 'twoButton')
        twoButton.clicked.connect(self.two_button_clicked)

        threeButton = self.window.findChild(QPushButton, 'threeButton')
        threeButton.clicked.connect(self.three_button_clicked)

        zeroButton = self.window.findChild(QPushButton, 'zeroButton')
        zeroButton.clicked.connect(self.zero_button_clicked)

        divideButton = self.window.findChild(QPushButton, 'divideButton')
        divideButton.clicked.connect(self.divide)

        #show window to user
        self.window.show()

    def seven_button_clicked(self):
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(sevenButton.text())

    def eight_button_clicked(self):
        eightButton = self.window.findChild(QPushButton, 'eightButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(eightButton.text())

    def nine_button_clicked(self):
        nineButton = self.window.findChild(QPushButton, 'nineButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(nineButton.text())

    def four_button_clicked(self):
        fourButton = self.window.findChild(QPushButton, 'fourButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(fourButton.text())

    def five_button_clicked(self):
        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(fiveButton.text())

    def six_button_clicked(self):
        sixButton = self.window.findChild(QPushButton, 'sixButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(sixButton.text())

    def one_button_clicked(self):
        oneButton = self.window.findChild(QPushButton, 'oneButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(oneButton.text())

    def two_button_clicked(self):
        twoButton = self.window.findChild(QPushButton, 'twoButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(twoButton.text())

    def three_button_clicked(self):
        threeButton = self.window.findChild(QPushButton, 'threeButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(threeButton.text())

    def zero_button_clicked(self):
        zeroButton = self.window.findChild(QPushButton, 'zeroButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(zeroButton.text())

    def divide(self):
        divideButton = self.window.findChild(QPushButton, 'divideButton')
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText(divideButton.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('calculator.ui')
    sys.exit(app.exec_())