import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont



# 引脚配置，按照上面的接线来配置
RST=23
DC=24
# 因为连的是CE0，这里的PORT和DEVICE也设置为0
SPI_PORT=0
SPI_DEVICE=0

#根据自己的oled型号进行初始化，我的是128X64、SPI的oled，使用SSD1306_128_64初始化
disp=Adafruit_SSD1306.SSD1306_128_64(rst=RST,dc=DC,spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display() #清屏

width=disp.width
height=disp.height

#font1=ImageFont.load_default() #Default Font
font = ImageFont.truetype("/home/pi/Documents/PI project/door lock/Fonts/simfang.ttf", 20, encoding="unic")  # 设置字体
font2 = ImageFont.truetype("/home/pi/Documents/PI project/door lock/Fonts/simfang.ttf", 15, encoding="unic") 

#指纹验证成功!
def finger(text):
    finger=Image.new('1',(width,height))
    draw_finger=ImageDraw.Draw(finger)
    draw_finger.text((0,0), text,font=font,fill=1)
    draw_finger.text((0,20),'指纹验证成功!',font=font,fill=1)
    disp.image(finger)
    disp.display()

#人脸识别中...
def face(text):
    face=Image.new('1',(width,height))
    draw_face=ImageDraw.Draw(face)
    draw_face.text((0,0),text,font=font,fill=1)
    draw_face.text((0,20),'人脸验证成功!',font=font,fill=1)
    disp.image(face)
    disp.display()

#蓝牙解锁成功!
def bluetooth():
    bluetooth=Image.new('1',(width,height))
    draw_bluetooth=ImageDraw.Draw(bluetooth)
    draw_bluetooth.text((0,20),'蓝牙解锁成功!',font=font,fill=1)
    disp.image(bluetooth)
    disp.display()

#验证失败!
def fail(text):
    fail=Image.new('1',(width,height))
    draw_fail=ImageDraw.Draw(fail)
    draw_fail.text((0,20),text+'验证失败!',font=font,fill=1)
    disp.image(fail)
    disp.display()

def cd():
    cd=Image.new('1',(width,height))
    draw_cd=ImageDraw.Draw(cd)
    draw_cd.text((0,10),'人脸识别冷却中...',font=font2,fill=1)
    draw_cd.text((0,30),'请蓝牙或指纹解锁!',font=font2,fill=1)
    disp.image(cd)
    disp.display()

def clear():
    disp.clear()
    disp.display()