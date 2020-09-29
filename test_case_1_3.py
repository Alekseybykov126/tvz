    # это нужно для проверки активной подписки без регистрации
    # emailt = "ttvzavr126@mail.ru"
    # passw = '111111'
    # summa = "1"
    # name = "Proxy Test"
    # time.sleep(2)
    # self.page.click_f('Клик_Вход', 1)
    # time.sleep(1)
    # self.page.send_f('Ввод_логина_вход', emailt, 2)
    # time.sleep(2)
    # self.page.send_f('Ввод_пароля_вход', passw, 3)
    # time.sleep(2)
    # self.page.click_f('Клик_Войти_auth', 4)
    # time.sleep(3)

from .page import *

time.sleep(2)
def case_1_3(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 1_3  tvweb_new-1_3: Покупка подписки "Отключи рекламу на tvzavr!" \n')
    email = self.page.rand_mail('28')[0]
    rand = self.page.rand_mail('28')[1]
    name = rand + '28 WebTvzavr'
    passw = '333333'

    name_card = 'ALEKSEI BYKOV'
    
    self.page.click_f('Клик_Вход', 1)
    time.sleep(1)
    self.prof.click_f('Клик_Регистрация', 2)
    time.sleep(1)
    
    #self.page.send_f('Ввод_логина', email, 3)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__address textbox"]').send_keys(email)
    time.sleep(2)
    
    #self.page.send_f('Ввод_пароля', passw, 4)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__password textbox"]').send_keys(passw)
    time.sleep(2)
    self.prof.click_f('Клик_Зарегистрироваться', 5)
    time.sleep(3)

    self.prof.click_f('Клик_значок_нового_пользователя', 6)
    time.sleep(2)

    remember_name = self.driver.find_element_by_xpath("//div[@class='profile-menu__name __username']") # запоминание имени пользователя
    remember_name = remember_name.get_attribute('innerHTML')
    print(remember_name)
    text = remember_name
    time.sleep(2)    

    self.page.click_f('Клик_Подписки', 6)
    resic = str(self.result.find_all_link("h1", "subscriptions__heading superheading-1")) # Проверка наличия текста Подписка tvzavr+
    assert ('Подписка «tvzavr+»') in resic  # проверочное словосочетание надписи
    self.page.loger_info('Наличие текста Подписка «tvzavr+» подтверждено')
    time.sleep(2)
    
    self.page.click_f('Клик_Подписка_Отключи_рекламу', 7)
    resic = str(self.result.find_all_link("h1", "subscriptions__heading superheading-1")) # Проверка наличия текста Подписка tvzavr+
    assert ('«Отключи рекламу на tvzavr!»') in resic  # проверочное словосочетание надписи
    self.page.loger_info('Наличие текста «Отключи рекламу на tvzavr!» подтверждено')
    time.sleep(8)      

    self.driver.find_element_by_xpath('//*[@id="disabled-ads"]/div[1]/div/div/div[2]/button[2]').click()   
    time.sleep(2)
    self.page.input_card('5599005033890711', '8', '2020', name_card, '526')
    time.sleep(5)

    self.page.waitForElementVisible('.//span[@class="subscriptions__duration"]', 10) # Проверка наличия информации о подписке
    res_txt = str(self.result.find_link("span", "subscriptions__duration"))
    assert ('Активна') in res_txt # Проверка наличия слова активна
    self.page.loger('Наличие покупки подтверждено')
    time.sleep(2)

    self.page.delete_uzer(remember_name) # Удаление пользователя
    self.page.loger('Пользователь ' + remember_name + ' удален')
    time.sleep(2)
    
    self.driver.quit()    
