from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from FinalWin import FinalScreen      
class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appears() #настраиваем окно
        self.initUI()      #щбьявляются виджеты
        self.connects()    #подключение обработчиков событий
        self.show()        #показать окно
    def set_appears(self):
        self.setWindowTitle(title1)
        self.resize(w,h)
        self.move(x,y)  
    def initUI(self):
        self.label1 = QLabel(txt_name)    
        self.label2 = QLabel(txt_age)    
        self.label3 = QLabel(txt_test1)
        self.label4 = QLabel(txt_test2)
        self.label5 = QLabel(txt_test3 )
        self.btn1 = QPushButton(txt_starttest1)
        self.btn2 = QPushButton(txt_starttest2 )
        self.btn3 = QPushButton(txt_starttest3)
        self.btn4 = QPushButton(txt_sendresults)  
        self.line_edit1 = QLineEdit(txt_hintname )
        self.line_edit2 = QLineEdit(txt_hinttest1)
        self.line_edit3 = QLineEdit(txt_hinttest1)
        self.line_edit4 = QLineEdit(txt_hinttest1)       
        self.line_edit5 = QLineEdit(txt_hinttest1)   

        self.h1 = QHBoxLayout()
        self.v1 = QVBoxLayout()
        self.v2 = QVBoxLayout()  

        self.v1.addWidget(self.label1,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit1,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label2,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit2,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label3,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn1,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit3,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label4,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn2,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label5,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn3,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit4,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit5,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn4,alignment= Qt.AlignCenter)

        self.setLayout(self.v1)
        self.setLayout(self.v2)
    def connects(self):
        self.btn4.clicked.connect(self.next)

    def next(self):
        self.hide()
        self.final = FinalScreen()     


