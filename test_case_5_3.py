from .page import * 
import time
from selenium import webdriver

time.sleep(2)
def case_5_3(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 5_3 tvweb_new-5_3: Проверка регистрации по номеру телефона \n')
    emailgo = 'bykov.a@tvzavr.ru'
    passok = 'tmW9HZvaksgc'
    
    phone = '79776410337'

    self.page.click_f('Клик_Вход', 1)
    time.sleep(2)
    self.prof.click_f('Клик_Регистрация', 2)
    time.sleep(1)
    self.page.click_f('По_номеру_телефона', 3)
    time.sleep(2)           
    self.page.send_f('Ввод_номера_телефона_reg', phone, 4)
    time.sleep(2)
   
    password_sms_1 = self.page.code_phone(phone)    #numberphone_7       Получение кода из СМС
    time.sleep(2)
    
    self.page.send_f('Ввод_СМС_пароля_reg', password_sms_1, 5)
    time.sleep(2)
    self.prof.click_f('Клик_phone_Зарегистрироваться', 6)
    time.sleep(7)

    self.prof.click_f('Клик_значок_нового_пользователя', 7) 
    time.sleep(2)

    resic = str(self.result.find_link("div", "profile-menu__name __username")) # Проверка авторизации пользователя
    assert ('79776410337') in resic # проверочное словосочетание надписи
    self.page.loger('Авторизация зарегистрированного пользователя по номеру телефона  ' + phone + 'подтверждена')
    time.sleep(2)

    self.prof.click_f('Клик_Выйти', 8)
    time.sleep(3)

    self.page.click_f('Клик_Вход', 9)
    time.sleep(2)

    self.page.send_f('Ввод_номера_телефона_auth', phone, 10)
    time.sleep(1)
    self.page.send_f('Ввод_из_СМС_пароля_auth', password_sms_1, 11)
    time.sleep(2)
    self.page.click_f('Клик_Войти_auth', 12)
    time.sleep(3)

    self.prof.click_f('Клик_значок_нового_пользователя', 13)
    resic = str(self.result.find_link("div", "profile-menu__name __username")) # Проверка авторизации пользователя
    self.page.loger('Номер пользователя: ' + resic)
    assert (phone) in resic  # проверочное словосочетание надписи
    self.page.loger_info('Авторизация пользователя  подтверждена')
    time.sleep(1)
    self.prof.click_f('Клик_Выйти', 14)

    # Удаление пользователя из админки 

    self.page.loger_info('Шаг 15 Удаление пользователя из админки')  

    self.driver.execute_script("window.open('','_blank');")
    time.sleep(2)
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    self.driver.get("https://www.tvzavr.ru:8080/admin/")
    time.sleep(2)
    # 'Открытие страницы админки
    self.page.loger_info('Открытие страницы админки')
    time.sleep(2)
    self.driver.maximize_window()
    time.sleep(2)
    self.driver.implicitly_wait(7)
    self.admin.click_f('Админка_большая_красная_кнопка', 14)
    time.sleep(2)
    # Логинимся через Google
    self.page.loger_info('Логинимся через Google')
    time.sleep(2)
    self.page.login_google(emailgo, passok)
    time.sleep(2)
    self.page.loger_info('Вошли в админку')
    time.sleep(3)
    self.admin.click_f('Профили_посетителей', 15)
    time.sleep(2)
    self.page.send_f('Админка_Ввод_в_поиск', phone, 16)
    time.sleep(2)
    self.admin.click_f('Админка_клик_найти', 17)
    time.sleep(2)
    self.admin.click_f('Админка_клик_чекбокс_1', 18)
    time.sleep(2)
    self.admin.click_f('Админка_Действие', 19)
    time.sleep(2)
    self.admin.click_f('Админка_Выбор_Удалить_пользователя', 20)
    time.sleep(2)
    self.admin.click_f('Админка_Выполнить', 21)
    time.sleep(2)
    self.admin.click_f('Админка_подтвердить', 22)
    time.sleep(2)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)
    self.driver.quit()