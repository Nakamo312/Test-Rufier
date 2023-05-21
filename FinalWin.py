from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
    
class FinalScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appears() #настраиваем окно
        self.initUI()      #щбьявляются виджеты
        self.show()        #показать окно
    def set_appears(self):
        self.setWindowTitle(title1)
        self.resize(w,h)
        self.move(x,y)  
    def initUI(self):
        self.lbl1 = QLabel(txt_index)
        self.lbl2 = QLabel(txt_workheart)

        self.v1 = QVBoxLayout()

        self.v1.addWidget(self.lbl1)
        self.v1.addWidget(self.lbl2)

        self.setLayout(self.v1)
