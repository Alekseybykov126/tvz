from .page import * 

time.sleep(2)
def case_5_2(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 5_2 tvweb_new-5_2: Проверка работоспособности элементов окошка пользователя, личный кабинет  \n')

    emailt = 'ttvzavr126@mail.ru'
    passw = '111111'
    
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
    time.sleep(2)

    self.driver.find_element_by_xpath('.//span[@class="__userbalance currency- currency currency-RUB"]').click() # Клик на кошелёк
    self.page.loger('Шаг 6. Клик на кошелёк')
    time.sleep(7)

    self.page.waitForElementVisible('.//div[@class="cabinet__content cabinet-account"]', 30) # Проверка перехода и содержание страницы
    res_txt = str(self.result.find_link("div", "cabinet__content cabinet-account"))
    assert('Баланс') in res_txt
    assert('Пополнить счёт') in res_txt
    assert('Программа лояльности') in res_txt
    assert('Промокод') in res_txt
    assert('Бонусная программа') in res_txt
    self.page.loger('Переход в кошелёк и содержание страницы подтверждено')
    time.sleep(3)

    self.page.loger('Шаг 7. Проверка Истории платежей')
    self.driver.find_element_by_xpath('.//button[@class="cabinet-balance__history button button_light button_stretched"]').click()  # Проверка окна истории платежей
    time.sleep(4)
    self.page.waitForElementVisible('.//div[@class="modal__content payment-history js-modal-content modal__content_open"]', 30) # Проверка появления окна
    res_txt = str(self.result.find_link("div", "modal__content payment-history js-modal-content modal__content_open"))
    assert('История платежей') in res_txt
    self.page.loger('Появление окна истории платежей подтверждено')
    time.sleep(3)

    self.page.waitForElementVisible('.//td[@class="payment-history__cell payment-history__cell_description"]', 30) # Проверка наличия платежа
    self.page.loger('Наличие платежа в истории подтверждено')
    time.sleep(3)

    self.page.loger('Шаг 8. Клик на покупки')
    self.driver.find_element_by_xpath('.//button[@data-sort-type="2"]').click() # Клик на покупки
    time.sleep(3)
    self.page.waitForElementVisible('.//td[@class="payment-history__cell payment-history__cell_description"]', 30) # Проверка наличия платежа
    self.page.loger('Наличие платежей в покупках подтверждено')
    time.sleep(3)

    self.page.loger('Шаг 9. Клик на Пополнения')
    self.driver.find_element_by_xpath('.//button[@data-sort-type="1"]').click() # Клик на пополнения
    time.sleep(3)
    self.page.waitForElementVisible('.//td[@class="payment-history__cell payment-history__cell_description"]', 30) # Проверка наличия пополнений
    self.page.loger('Наличие пополнений счета подтверждено')
    time.sleep(3)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # Клик на крестик
    time.sleep(3)

    self.prof.click_f('Клик_значок_пользователя', 10)
    time.sleep(3)
    self.page.loger('Шаг 11. Клик на счет') 
    self.driver.find_element_by_xpath('.//a[@href="/profile/#tab=cabinet-account"]').click() # Клик на счет
    time.sleep(6)
    res_txt = str(self.result.find_link("div", "cabinet__content cabinet-account"))
    assert('Баланс') in res_txt
    self.page.loger('Переход в счет подтвержден')    
    time.sleep(3)

    self.page.loger('Шаг 12. Клик на "Узнать подробности" в программе лояльности')
    self.driver.find_element_by_xpath('.//a[@class="cabinet-loyalty__about button button_light button_stretched"]').click() # Клик на узнать подробности программа лояльности
    time.sleep(4)
    self.page.waitForElementVisible('.//h1[@class="loyalty__heading heading-1"]', 30) # Проверка перехода на страницу программы лояльности
    self.page.loger('Переход на страницу программы лояльности подтвержден')
    #self.driver.back()
    time.sleep(5)

    self.prof.click_f('Клик_значок_пользователя', 13)
    time.sleep(3)

    self.page.loger('Шаг 14. Клик на бонусную программу')
    self.driver.find_element_by_xpath('.//a[@href="/loyalty/"]').click() # Клик на бонусную программу из окна пользователя
    time.sleep(3)

    self.page.waitForElementVisible('.//div[@class="loyalty__rewards loyalty-rewards"]', 10)
    self.page.loger('Переход на страницу Бонусной программы подтвержден')
    
    self.prof.click_f('Клик_значок_пользователя', 15)
    time.sleep(3)

    self.page.loger('Шаг 16. Клик на подписки')
    self.driver.find_element_by_xpath('.//a[@href="/profile/#tab=cabinet-subscriptions"]').click() # Клик на подписки
    time.sleep(5)

    self.page.waitForElementVisible('.//h2[@class="cabinet__heading heading-2"][contains(., "Подписки")]', 30) # Проверка наличия надписи Подписки
    self.page.waitForElementVisible('.//div[@class="cabinet-subscriptions__item subscription-card"]', 30) # Проверка наличия подписок
    self.page.loger('Переход на вкладку подписки подтвержден')
    time.sleep(2)

    self.prof.click_f('Клик_значок_пользователя', 17)
    time.sleep(3)

    self.page.loger('Шаг 18. Проверка перехода на страницу/раздел мои фильмы')
    self.driver.find_element_by_xpath('.//a[@href="/profile/#tab=cabinet-clips"]').click()  # Клик на "Мои фильмы"
    time.sleep(3)
    # Проверка перехода и содержания
    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2"][contains(., "Купленные фильмы")]', 30) # купленные фильмы
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2"][contains(., "Избранное")]', 30) # Избранное
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2"][contains(., "История просмотра")]', 30) # История просмотра
    self.page.loger('Переход в "Мои фильмы" и содежание страницы подтверждено')
    time.sleep(2)

    self.prof.click_f('Клик_значок_пользователя', 19)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//a[@href="/profile/#tab=cabinet-settings"]').click() # Клик настройки
    time.sleep(4)

    self.page.waitForElementVisible('.//h2[@class="cabinet__heading heading-2"][contains(., "Личные данные")]', 30) 
    time.sleep(1)
    self.page.waitForElementVisible('.//div[@class="cabinet-information__label"]', 30) 
    time.sleep(1)
    self.page.waitForElementVisible('.//h2[@class="cabinet__heading heading-2"][contains(., "Смена пароля")]', 30) 
    self.page.loger('Переход на страницу "Настройки" и содержание страницы подтверждено')
    time.sleep(1)

    self.prof.click_f('Клик_значок_пользователя', 20)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//a[@href="/profile/#tab=cabinet-devices"]').click() # Клик Мои устройства
    time.sleep(3)

    self.page.waitForElementVisible('.//div[@class="cabinet-binding__heading cabinet__heading heading-2"]', 30)
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@class="cabinet-binding__subheading subheading-1"]', 30)
    self.page.loger('Переход на страницу "Мои устройства" и содержание страницы подтверждено')
    time.sleep(2)
    self.driver.quit()   