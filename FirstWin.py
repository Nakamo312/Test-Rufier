from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from SecondWin import SecondWin

from instr import *
class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appears()
        self.initUI()
        self.connects()
        self.show()
    def set_appears(self):
        self.setWindowTitle(title1)
        self.resize(w,h)
        self.move(x,y)  
    def initUI(self):
        self.label1 = QLabel(text1)
        self.label2 = QLabel(instr) 
        self.to_second = QPushButton('Далее')
        self.l1 = QVBoxLayout()

        self.l1.addWidget(self.label1)
        self.l1.addWidget(self.label2)
        self.l1.addWidget(self.to_second)

        self.setLayout(self.l1)

    def connects(self):
        self.to_second.clicked.connect(self.next)
    def next(self):
        self.hide()
        self.second = SecondWin()     


app = QApplication([])  

window = FirstScreen()

app.exec()
