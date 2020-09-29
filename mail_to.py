import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'dubodelov.a@tvzavr.ru'
email_password = 'QwertyQwerty_123'
email_to = ['tvzavrtest.test@gmail.com']
dir_path = "C:/Users/user/PycharmProjects/Projekt_Smart/PC"
files = ["log.html", "report.html"]

subject = 'Отчет по регрессивному тестированию WEB tvzavr.ru '
for email_send in email_to:
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    print('Отправляю', email_send)
    body = 'Письмо сформировано автоматически. Скачать файлы. Сначала открывать report. Если все зеленое - все ОК. Если все красное, то причина в log.html'
    msg.attach(MIMEText(body, 'plain'))

    for filename in files:
        # filename = 'log.html'
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)
        text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()