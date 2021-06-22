from aip import AipFace
from picamera import PiCamera
import urllib.request
import RPi.GPIO as GPIO
import base64
import time
import OLED
#百度人脸识别API账号信息
APP_ID = '24388578'
API_KEY = 'HFqiu0YEA40D0G5CPzHxGzD3'
SECRET_KEY ='OfbdW3GKQljhTcQK6vrXZxb2N8oY3wpD'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云
#图像编码方式
IMAGE_TYPE='BASE64'
camera = PiCamera()#定义一个摄像头对象
#用户组
GROUP = 'zjsu'
 
#照相函数
def getimage():
    camera.resolution = (1024,768)#摄像界面为1024*768
    camera.start_preview()#开始摄像
    camera.capture('faceimage.jpg')#拍照并保存
#对图片的格式进行转换
def transimage():
    f = open('faceimage.jpg','rb')
    img = base64.b64encode(f.read())
    return img
#上传到百度api进行人脸检测
def go_api(image):
    result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP);#在百度云人脸库中寻找有没有匹配的人脸
    if result['error_msg'] == 'SUCCESS':#如果成功了
        name = result['result']['user_list'][0]['user_id']#获取名字
        score = result['result']['user_list'][0]['score']#获取相似度
        print("score:"+str(score))
        if score > 70:#如果相似度大于80
            if name == 'pms':
                print("欢迎%s !" % name)
                time.sleep(3)
            if name == 'lsd':
                print("欢迎%s !" % name)
                time.sleep(3)
            return name
        else:
            print("对不起，我不认识你！")
            name = 'Unknow'
            return 0
    if result['error_msg'] == 'pic not has face':
        print('检测不到人脸')
        OLED.fail('人脸')
        time.sleep(2)
        return -2
    else:
        print(str(result['error_code'])+' ' + str(result['error_code']))
        return -1
#人脸识别 识别成功返回1 识别失败返回0
def identify():
    print('开始识别')
    getimage()#拍照
    img = transimage()#转换照片格式
    res = go_api(img)#将转换了格式的图片上传到百度云
    if res == 0 or res == -1:
        print("关门")
    else:
        print("开门")
    return res
