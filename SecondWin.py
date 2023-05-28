from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont 


name =''
age = 0
p1 = 0
p2 = 0
p3 = 0
class Expirements():
    name =''
    age = 0
    p1 = 0
    p2 = 0
    p3 = 0

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
        self.text_timer = QLabel(txt_timer)

        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        
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
        self.v1.addWidget(self.btn1,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label3,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit3,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label4,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn2,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.label5,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn3,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit4,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.line_edit5,alignment= Qt.AlignLeft)
        self.v1.addWidget(self.btn4,alignment= Qt.AlignCenter)

        self.v2.addWidget(self.text_timer,alignment= Qt.AlignRight)
        self.h1.addLayout(self.v1)
        self.h1.addLayout(self.v2)
        self.setLayout(self.h1)
    def connects(self):
        self.btn1.clicked.connect(self.timer_test) 
        self.btn2.clicked.connect(self.timer_test2) 
        self.btn3.clicked.connect(self.timer_test3) 
        self.btn4.clicked.connect(self.next)

    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer() 
        self.timer.timeout.connect(self.timer1event)
        self.timer.start(1000)
    def timer_test2(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer() 
        self.timer.timeout.connect(self.timer2event)
        self.timer.start(1500)

    def timer_test3(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer() 
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)   

    def timer1event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop() 
    def timer2event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()       
    def timer3event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >=45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif  int(time.toString('hh:mm:ss')[6:8]) <=15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")      
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()                

    def next(self):
        Expirements.name = self.line_edit1.text()
        Expirements.age=   int(self.line_edit2.text())
        Expirements.p1 =   int(self.line_edit3.text())
        Expirements.p2 =   int(self.line_edit4.text())
        Expirements.p3 =   int(self.line_edit5.text())
        self.hide()
        self.final = FinalScreen()     


from ruffier import *

class FinalScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appears() #настраиваем окно
        self.initUI()      #щбьявляются виджеты
        self.show() 
    def set_appears(self):
        self.setWindowTitle(title1)
        self.resize(w,h)
        self.move(x,y)  
    def initUI(self):        
        self.lbl1 = QLabel(txt_index + str(calc_Index(Expirements.p1,Expirements.p2,Expirements.p3)) )
        self.lbl2 = QLabel(txt_workheart + result(calc_Index(Expirements.p1,Expirements.p2,Expirements.p3),Expirements.age))

        self.v1 = QVBoxLayout()

        self.v1.addWidget(self.lbl1,alignment= Qt.AlignCenter)
        self.v1.addWidget(self.lbl2,alignment= Qt.AlignCenter)

        self.setLayout(self.v1)

