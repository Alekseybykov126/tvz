from .page import * 

time.sleep(1)
def case_1_4(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 1_4 tvweb_new-1_4: Пополнение личного счета с карты на 1 рубль \n')

    emailt = 'ttvzavr126@mail.ru'
    passw = '111111'
    
    summa = "1"
    name = "Proxy Test"

    time.sleep(2)
    self.page.click_f('Клик_Вход', 1)
    time.sleep(1)
    #self.page.send_f('Ввод_логина_вход', emailt, 2)
    self.driver.find_element_by_xpath('.//input[@class="authorization__login textbox"]').send_keys(emailt)
    time.sleep(2)

    #self.page.send_f('Ввод_пароля_вход', passw, 3)
    self.driver.find_element_by_xpath('.//input[@class="authorization__password textbox"]').send_keys(passw)
    time.sleep(2)
    
    self.page.click_f('Клик_Войти_auth', 4)
    time.sleep(2)

    self.prof.click_f('Клик_значок_пользователя', 5)

    cash_1 = self.driver.find_element_by_xpath("//span[@class='__userbalance currency- currency currency-RUB']") # проверка личного счета до пополнения
    cash_1 = cash_1.get_attribute('innerHTML')
    self.page.loger('Счёт до пополнения: ' + cash_1)
    cash_1 = int(cash_1)

    time.sleep(1)
    self.prof.click_f('Клик_Личный_счет', 6)
    time.sleep(1)

    self.prof.click_f('Клик_Пополнить', 7)
    time.sleep(2)
    self.page.send_f('Ввод_суммы_пополнения_счета', summa, 8)
    time.sleep(2) 
    self.card.click_f('Клик_Оплатить_личный_счет', 9) # подразумевается, что карта для оплаты сохранена
    time.sleep(15)  # время на прохождение оплаты
    self.prof.click_f('Клик_значок_пользователя', 10)
    time.sleep(1)

    cash_2 = self.driver.find_element_by_xpath("//span[@class='__userbalance currency- currency currency-RUB']") # проверка личного счета после пополнения
    cash_2 = cash_2.get_attribute('innerHTML')
    self.page.loger('Счёт после пополнения: ' + cash_2)
    cash_2 = int(cash_2)

    if cash_1 < cash_2:
        self.page.loger('Счёт успешно пополнен!')
    else:
        self.page.loger('Счёт не пополнен')
        assert()

    self.prof.click_f('Клик_Выйти', 11)
    time.sleep(1)
    self.driver.quit()