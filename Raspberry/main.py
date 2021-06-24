import serial
import time
import RPi.GPIO as GPIO
import OLED
import face_identification as fi
import DBmethods as db
import os
import textTovoice
import sendEmail as sd

ser = serial.Serial('/dev/ttyACM0', 9600,timeout=1);
face_cnt = 0
face_bool = True
db.init()
try:
    while 1:
        text=ser.readline()
        text=text.decode("UTF-8")
        print(text)
        if text == 'nullFinger\r\n':
            OLED.fail('指纹')
        elif text == '1\r\n'or text=='2\r\n':
            OLED.finger('李晟迪')
            db.insert('李晟迪','指纹')
            if not face_bool:
                face_cnt=0
                face_bool = True
        elif text == '3\r\n'or text=='4\r\n':
            OLED.finger('潘淼森')
            db.insert('潘淼森','指纹')
            if not face_bool:
                face_cnt=0
                face_bool = True
        elif text == 'BLE\r\n':
            OLED.bluetooth()
            db.insert('管理员','蓝牙')
            if not face_bool:
                face_cnt=0
                face_bool = True
        elif text == 'startAlarm\r\n':
            fi.getimage()
            sd.send_email_by_qq('shengdi_li@qq.com')
        elif text == 'face\r\n':
            if face_bool:
                res = fi.identify()
                if res == 'pms':
                    OLED.face('潘淼森')
                    db.insert('潘淼森','人脸')
                    ser.write('o'.encode())
                    face_cnt = 0
                elif res == 'lsd':
                    OLED.face('李晟迪')
                    db.insert('李晟迪','人脸')
                    ser.write('o'.encode())
                    face_cnt = 0
                elif res == 0:
                    os.system('mpg123 ooo.mp3')
                    OLED.fail('人脸')
                    face_cnt+=1
                elif res==-2:
                    OLED.fail('人脸')
                    face_cnt+=1
                if face_cnt == 3:
                    face_bool = False
            else:
                OLED.cd()
        elif text=='Sound\r\n':
            tmp = db.select()
            textTovoice.t2a(tmp)
            os.system('mpg123 result.mp3')
            
except KeyboardInterrupt() as results: #Ctrl+C停止
    OLED.clear()
    ser.close()