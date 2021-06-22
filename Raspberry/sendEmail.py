#coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email_by_qq(to):
    sender_mail = '929123714@qq.com'
    sender_pass = 'ccnuqpcpiduzbcaj'

 
    msg_root = MIMEMultipart('mixed')

    msg_root['From'] = 'shengdi_li@foxmail.com<929123714@qq.com>'
    msg_root['To'] = to
    subject = '危险⚠️️！门禁报告！'
    msg_root['subject'] = Header(subject, 'utf-8')

    text_info = '智能门锁已查获以下企图闯入您住所的人员-PythonTest'
    text_sub = MIMEText(text_info, 'plain', 'utf-8')
    msg_root.attach(text_sub)

    #


    image_file = open('./faceimage.jpg', 'rb').read()
    image = MIMEImage(image_file)
    image.add_header('Content-ID', '<image1>')

    image["Content-Disposition"] = 'attachment; filename="red_people.png"'
    msg_root.attach(image)



    try:
        sftp_obj =smtplib.SMTP('smtp.qq.com', 25)
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, to, msg_root.as_string())
        sftp_obj.quit()
        print('sendemail successful!')

    except Exception as e:
        print('sendemail failed next is the reason')
        print(e)