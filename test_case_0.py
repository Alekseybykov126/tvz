

#  test-case-25 ПРОВЕРЯЕТ РЕГИСТРАЦИЮ ПО НОМЕРУ ТЕЛЕФОНА



from Regress_web.page import *  #Regress_web.
import time
from selenium import webdriver

def case_0(self, full_screen):
    print('Запуск Тест кейс № 25 tvweb_new-25:Проверка регистрации по номеру телефона')
    emailgo = 'bykov.a@tvzavr.ru'
    passok = 'tmW9HZvaksgc'
    page = MainPage(self.driver)
    prof = Profile(self.driver)
    card = CardFilm(self.driver)
    result = ResultPage(self.driver)
    admin = Admin(self.driver)
    if full_screen == 1:
        page.click_f('Клик_кнопки_крестик', 5)
        print('Закрыто окно full screen')
    else:
        print('нет акции')

    # self.driver.close()
    # driver = webdriver.Chrome()
    self.driver.get("https://www.tvzavr.ru:8080/admin/")
    # 'Открытие страницы админки
    page.loger_info('Открытие страницы админки')
    self.driver.maximize_window()
    self.driver.implicitly_wait(12)
    self.driver.find_element_by_css_selector('body > div > section > a').click()
    time.sleep(5)
    # Логинимся через Google
    page.loger_info('Логинимся через Google')
    page.login_google(emailgo, passok)
    page.loger_info('Вошли в админку')
    admin.click_f('Профили_посетителей', 15)
    page.send_f('Админка_Ввод_в_поиск', numberphone_7, 16)
    admin.click_f('Админка_клик_найти', 17)
    admin.click_f('Админка_клик_чекбокс_1', 18)
    admin.click_f('Админка_Действие', 19)
    admin.click_f('Админка_Выбор_Удалить_пользователя', 20)
    admin.click_f('Админка_Выполнить', 21)
    admin.click_f('Админка_подтвердить', 22)
    time.sleep(5)
