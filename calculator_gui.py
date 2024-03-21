from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
from calculator import Calculator

class Calculator_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.input_numbers = []

        self.setFixedSize(371, 300)
        self.centralwidget = QWidget(self)
        self.lcd_screen = QLCDNumber(9,self.centralwidget)
        self.lcd_screen.setGeometry(QRect(0, 0, 371, 51))
        

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(10, 50, 349, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        


        self.button_1 = QPushButton("1",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)
        self.button_1.clicked.connect(lambda: self.numberPressed(1))


        self.button_2 = QPushButton("2",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_2, 0, 1, 1, 1)
        self.button_2.clicked.connect(lambda: self.numberPressed(2))


        self.button_3 = QPushButton("3",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_3, 0, 2, 1, 1)
        self.button_3.clicked.connect(lambda: self.numberPressed(3))

        self.button_4 = QPushButton("4",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)        
        self.button_4.clicked.connect(lambda: self.numberPressed(4))

        self.button_5 = QPushButton("5",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)
        self.button_5.clicked.connect(lambda: self.numberPressed(5))

        self.button_6 = QPushButton("6",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)
        self.button_6.clicked.connect(lambda: self.numberPressed(6))

        self.button_7 = QPushButton("7",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)
        self.button_7.clicked.connect(lambda: self.numberPressed(7))

        self.button_8 = QPushButton("8",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)
        self.button_8.clicked.connect(lambda: self.numberPressed(8))

        self.button_9 = QPushButton("9",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)
        self.button_9.clicked.connect(lambda: self.numberPressed(9))


        self.button_0 = QPushButton("0",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_0, 3, 1, 1, 1)
        self.button_0.clicked.connect(lambda: self.numberPressed(0))

        self.button_c = QPushButton("C",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_c, 3, 0, 1, 1)
        self.button_c.clicked.connect(self.delete)

        self.button_equal = QPushButton("=",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_equal, 3, 2, 1, 1)
        self.button_equal.clicked.connect(self.equal)

        self.button_plus = QPushButton("+",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_plus, 0, 3, 1, 1)
        self.button_plus.clicked.connect(lambda:self.calculator.operatorSettled('+'))

        self.button_minus = QPushButton("-",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_minus, 1, 3, 1, 1)
        self.button_minus.clicked.connect(lambda:self.calculator.operatorSettled('-'))

        self.button_multiply = QPushButton("x",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_multiply, 2, 3, 1, 1)
        self.button_multiply.clicked.connect(lambda:self.calculator.operatorSettled('x'))

        self.button_div = QPushButton("÷",self.gridLayoutWidget)
        self.gridLayout.addWidget(self.button_div, 3, 3, 1, 1)
        self.button_div.clicked.connect(lambda:self.calculator.operatorSettled('/'))

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 371, 22))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)


    def equal(self):
        result = self.calculator.equals()
        self.lcd_screen.display(result)

    def delete(self):
        self.calculator.clear()
        self.lcd_screen.display(str(self.calculator.showDigits()))

    def numberPressed(self, number):
        self.calculator.addDigit(number)
        n =str(self.calculator.showDigits())
        self.lcd_screen.display(n)

    def setOperator(self, operator):
        self.calculator.operatorSettled(operator)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Calculator_gui()
    test.show()
    sys.exit(app.exec())    
