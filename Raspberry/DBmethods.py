import sqlite3
import textTovioce
from playsound import playsound

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

def insert(id:str,time:str,way:str):
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

init()
insert('李晟迪', '6月14日14时35分', '蓝牙')
insert('黄陈雷', '6月14日14时42分', '指纹')
insert('叶轶楠', '6月14日14时43分', '人脸识别')
insert('尹珩宇', '6月14日14时52分', '指纹')
tmp = select()
textTovioce.t2a(tmp)
playsound('result.mp3')
