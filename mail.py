import smtplib, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from page import * # Regress_web.
from selenium import webdriver
from datetime import datetime


page = MainPage(webdriver)
time.sleep(5)
begin = datetime.now().time()
consol_brut = page.consol_jenkins()
# page.loger_info('consol = ' + consol_brut)
page.loger_info('begin = ' + str(begin))
midle = datetime.now().time()
page.loger_info('midle = ' + str(midle))
if "15 tests total, 15 passed, 0" in consol_brut: # Регресс прошел успешно
    consol_part = consol_brut.split('15 tests')[1]
    consol = consol_part.split('failed')[0]
    message = 'Автотест: Регресс прошел успешно: 15 tests ' + str(consol) + ' failed'
    page.loger_info(message)
    # page.scype_send_web('bodrec', 'br7pw222', message)
else:#                                              Регресс провален
    consol_part = consol_brut.split('15 tests')[1]
    consol = consol_part.split('failed')[0]
    message = 'Автотест: Результат регресс теста: 15 tests ' + str(consol) + ' failed'
    page.loger_info(message)
    # page.scype_send_web('bodrec', 'br7pw222', message)

email_user = 'dubodelov.a@tvzavr.ru'
email_password = 'QwertyQwerty_123'
email_send = 'tvzavrtest.test@gmail.com'
dir_path = "C:/Users/user/PycharmProjects/Projekt_Smart/PC"
files = ["log.html", "report.html"]

subject = 'Отчет по регрессивному тестированию WEB tvzavr.ru '

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
print('Отправляю письмо на почту ', email_send)
body = 'Автотест: Результат регресс теста: ' + str(consol) + ' failed. ' + 'Письмо сформировано автоматически. Скачать файлы. Сначала открывать report. Если все зеленое - все ОК. Если все красное, то причина в log.html'
msg.attach(MIMEText(body,'plain'))

for filename in files:
    # filename = 'log.html'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)
    text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
