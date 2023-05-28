from SecondWin import *
from instr import *
def calc_Index(p1,p2,p3):
    return (4*(p1+p2+p3)-200)/10

def result(index,age):
    if age == 7 or age == 8:
        if index >= 21:
            return txt_res1
        elif index < 21 and index >= 17:
            return txt_res2
        elif index < 17 and index >= 12:
            return txt_res3
        elif index < 12 and index >= 6.5:
            return txt_res4
        else:
            return txt_res5
    if age == 9 or age == 10:
        if index >= 19.5:
            return txt_res1
        elif index < 19.5 and index >= 15.5:
            return txt_res2
        elif index < 15.5 and index >= 10.5:
            return txt_res3
        elif index < 10.5 and index >= 5:
            return txt_res4
        else:
            return txt_res5
    if age == 11 or age == 12:
        if index >= 18:
            return txt_res1
        elif index < 18 and index >= 14:
            return txt_res2
        elif index < 14 and index >= 9:
            return txt_res3
        elif index < 9 and index >= 3.5:
            return txt_res4
        else:
            return txt_res5
    if age == 13 or age == 14:
        if index >= 16.5:
            return txt_res1
        elif index < 16.5 and index >= 12.5:
            return txt_res2
        elif index < 12.5 and index >= 7.5:
            return txt_res3
        elif index < 7.5 and index >= 2:
            return txt_res4
        else:
            return txt_res5
    if age >= 15:
        if index >= 15:
            return txt_res1
        elif index < 15 and index >= 11:
            return txt_res2
        elif index < 11 and index >= 6:
            return txt_res3
        elif index < 6 and index >= 0.5:
            return txt_res4
        else:
            return txt_res5
