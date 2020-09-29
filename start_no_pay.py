import subprocess
import time

subprocess.call(['pybot.bat', 'C:\\Users\\user\\.jenkins\\workspace\\1_Regress\\Regress_web\\test_suit_no_pay.robot'])
time.sleep(5)
subprocess.call(['python.exe', 'C:\\Users\\user\\.jenkins\\workspace\\1_Regress\\Regress_web\\mail.py'])


# Jenkins берет файлы из C:\Users\user\.jenkins\workspace\rf_No_Pay_Web_No_Pay>python No_Pay_Web
# а надо брать из C:\Users\user\.jenkins\workspace\rf_No_Pay_Web\No_Pay_Web так как сюда Git отправляет файлы.
#Ошибка возникает из за того, что имена проектов разные, а директория одна.
#Чтобы избежать ошибки, надо исправить директорию в настройках Дженкинс и создать отдельный проект в PyCharm

# https://web.skype.com/ru/


