#ccnuqpcpiduzbcaj
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email_by_qq(to):
    sender_mail = '929123714@qq.com'
    sender_pass = 'ccnuqpcpiduzbcaj'

    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')
    # 邮件添加的头尾信息等
    msg_root['From'] = '929123714@qq.com<929123714@qq.com>'
    msg_root['To'] = to
    # 邮件的主题，显示在接收邮件的预览页面
    subject = '☢︎危险⚠️！门禁报告📸！'
    msg_root['subject'] = Header(subject, 'utf-8')

    # 构造文本内容
    text_info = '智能门锁已查获以下企图闯入您住所的人员-PythonTest'
    text_sub = MIMEText(text_info, 'plain', 'utf-8')
    msg_root.attach(text_sub)

    #

    # 构造图片
    image_file = open('./IMG_6512.jpg', 'rb').read()
    image = MIMEImage(image_file)
    image.add_header('Content-ID', '<image1>')
    # 如果不加下边这行代码的话，会在收件方方面显示乱码的bin文件，下载之后也不能正常打开
    image["Content-Disposition"] = 'attachment; filename="red_people.png"'
    msg_root.attach(image)

    # # 构造附件
    # txt_file = open(r'D:\python_files\files\hello_world.txt', 'rb').read()
    # txt = MIMEText(txt_file, 'base64', 'utf-8')
    # txt["Content-Type"] = 'application/octet-stream'
    # #以下代码可以重命名附件为hello_world.txt
    # txt.add_header('Content-Disposition', 'attachment', filename='hello_world.txt')
    # msg_root.attach(txt)

    try:
        sftp_obj =smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, to, msg_root.as_string())
        sftp_obj.quit()
        print('sendemail successful!')

    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)


if __name__ == '__main__':
    # 可以是一个列表，支持多个邮件地址同时发送，测试改成自己的邮箱地址
    to = '1181044064@qq.com'
    send_email_by_qq(to)