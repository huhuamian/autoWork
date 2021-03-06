# -*- coding: utf-8 -*-
# @Time : 2020/8/23 2:22
# @公众号 :Python自动化办公社区 
# @File : 24_用Python发送带附件的邮件.py
# @Software: PyCharm
# @Description:

# -*- coding: utf-8 -*-
# @Time : 2020/8/23 2:15
# @公众号 :Python自动化办公社区
# @File : 23_用Python发送普通的文字邮件.py
# @Software: PyCharm
# @Description:

import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

host_server = 'smtp.sina.com'
sender_sina = 'your_email@sina.com'
pwd = 'your_pwd'

sender_sina_mail = 'your_email@sina.com'
receiver = 'others_email@sina.com'
mail_title = '这是标题'
mail_content = '这是正文'
msg = MIMEMultipart()
msg['Subject'] = Header(mail_title, 'utf-8')
msg['From'] = sender_sina_mail
msg['To'] = Header('mail_title', 'utf-8')
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
# 添加附件
attachment = MIMEApplication(open('student.xls', 'rb').read())
attachment.add_header('Content-Disposition', 'attachment', filename='student.xls')
msg.attach(attachment)
try:
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_sina, pwd)
    smtp.sendmail(sender_sina_mail, receiver, msg.as_string())
    smtp.quit()
    print('success')
except smtplib.SMTPException:
    print('error')
