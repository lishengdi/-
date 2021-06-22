import sqlite3
import textTovoice
from playsound import playsound
import time
import pygame
def init():
    conn = sqlite3.connect('Record.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS 'doorLog';")
    c.execute('''CREATE TABLE IF NOT EXISTS doorLog
           (ID TEXT ,
           TIME           TEXT    PRIMARY KEY,
           WAY            TEXT    );''')
    conn.commit()
    conn.close()

def insert(id:str,way:str):

    time=CreateTime()
    conn = sqlite3.connect('Record.db')
    c = conn.cursor()
    c.execute("INSERT INTO doorLog (ID,TIME,WAY) \
          VALUES (?,?,?)",(id,time,way))

    conn.commit()
    conn.close()

def select():
    people: str = ""
    data_base = sqlite3.connect('Record.db')
    ptr = data_base.cursor()
    List = ptr.execute("SELECT * from doorLog")
    for i in List:
        person: str = ""
        if i[0] == '':
            person += "未注册用户于"
        else:
            person += i[0] + "于"
        person += i[1]
        person += "通过" + i[2] + "的方式进入大门 "
        people += person;
    data_base.close()
    return people


def CreateTime():
    Time=time.strftime("%m月%d日 %H时%M分%S秒", time.localtime())
    return Time

# init()
# insert('李晟迪','蓝牙')
# #insert('黄陈雷','指纹')
# #insert('叶轶楠','人脸识别')
# #insert('尹珩宇','指纹')
# tmp = select()
# textTovoice.t2a(tmp)
# pygame.mixer.init()
# pygame.mixer.music.load('result.mp3')
# pygame.mixer.music.play()
# #playsound('result.mp3')




