# -*- coding: utf-8 -*-
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 获取scripts文件夹路径
scripts_dir = os.path.dirname(os.path.abspath(__file__))
# 获取reports文件夹路径
reports_dir = os.path.join(scripts_dir, '../reports/')
# 获取screenshots文件夹路径
screenshots_dir = os.path.join(scripts_dir, '../screenshots/')
# 获取logs文件夹路径
logs_dir = os.path.join(scripts_dir, '../logs/')


def send_email(un, pw, server, addresses):
    """
    发送邮件函数
    """
    msg = MIMEMultipart()
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    subject = 'Test finished at ' + now
    msg["Subject"] = subject
    msg["from"] = un
    msg["to"] = addresses
    count = 0

    # 将报告添加到邮件附件
    for filename in os.listdir(reports_dir):
        if '.html' in filename:
            f = MIMEApplication(open(reports_dir + filename, 'rb').read())
            f.add_header('Content-Disposition', 'attachment', filename=filename)
            count += 1
            msg.attach(f)

    # 将截图添加到邮件附件
    for filename in os.listdir(screenshots_dir):
        if '.png' in filename:
            f = MIMEApplication(open(screenshots_dir + filename, 'rb').read())
            f.add_header('Content-Disposition', 'attachment', filename=filename)
            count += 1
            msg.attach(f)

    # 将日志添加到邮件附件
    for filename in os.listdir(logs_dir):
        if '.log' in filename:
            f = MIMEApplication(open(logs_dir + filename, 'rb').read())
            f.add_header('Content-Disposition', 'attachment', filename=filename)
            count += 1
            msg.attach(f)

    msg.attach(MIMEText('Attachment: {}'.format(count), 'plain', _charset="utf-8"))

    smtp = smtplib.SMTP()
    smtp.connect(server)
    smtp.login(un, pw)
    smtp.sendmail(un, addresses.split(','), msg.as_string())
    smtp.quit()


if __name__ == '__main__':

    # 发送者邮箱账号
    username = '111@qq.com'
    # 发送者邮箱密码
    password = '111'
    # smtp服务器地址
    server_smtp = 'smtp.qq.com'
    # 接收者邮箱账号（多个账号用英文逗号隔开）
    addresses_receive = '222@163.com,333@126.com,444@qq.com,555@gmail.com'

    send_email(username, password, server_smtp, addresses_receive)
