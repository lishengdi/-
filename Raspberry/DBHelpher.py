import sqlite3

def createDB():
    data_base=sqlite3.connect('recordDB')
    cursor=data_base.cursor()
    cursor.execute('''create table if not exists doorLog(
                        identity text,
                        Time text,
                        method text
                        )''')
    data_base.commit()


def insert(name:str,time:str,way:str):
    data_base = sqlite3.connect('recordDB')
    ptr=data_base.cursor()
    ptr.execute("INSERT INTO doorLog (identity,Time,method) VALUES ('李晟迪','2021-6-14','蓝牙')")


insert('李晟迪','2021-6-14','蓝牙')