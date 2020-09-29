from Regress_web.page import*   # ДОДЕЛАТЬ просмотр ник нейма уже в личном кабинете

def case_4_1(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 4_1 tvweb_new-4_1: Авторизация через соцсети по ссылкам из окна авторизации \n')

    emailfb = 'tvzavrtest.test@yandex.ru'
    passfb = '315492'
    passok = 'Test315492'
    passgo = 'Test315496'
    emailgo = 'tvzavrtest.test@gmail.com'
    emailru = 'tvzavrtest.test@mail.ru'
    
    self.page.click_f('Клик_Вход', 1)
    time.sleep(3)

    self.page.click_f('Клик_Вход_через_FB', 2)
    time.sleep(3)
    #self.page.send_f('Ввод_логина', emailfb, 3)
    self.driver.find_element_by_xpath('.//input[@class="inputtext _55r1 inputtext _1kbt inputtext _1kbt"]').send_keys(emailfb)
    time.sleep(4)
    self.page.send_f('Ввод_пароля_FB', passfb, 4)
    time.sleep(4)
    self.page.click_f('Клик_Вход_FB', 5)
    time.sleep(11)

    #self.driver.refresh() # Обновление страницы
    self.prof.click_f('Клик_значок_пользователя', 6)
    #self.prof.click_f('Клик_значок_нового_пользователя', 6)
    time.sleep(5)
    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 15)
    resic = str(self.result.find_link("div", "profile-menu__name __username"))
    assert ('Тест20180827') in resic  # Тест тест - проверочное словосочетание надписи
    self.page.loger_info('Авторизация зарегистрированного на фейсбук пользователя Тест тест подтверждена')
    self.prof.click_f('Клик_Выйти', 7)
    time.sleep(3)

    self.page.click_f('Клик_Вход', 8)
    time.sleep(3)
    self.page.click_f('Клик_Вход_через_VK', 9)
    time.sleep(4)
    #self.page.send_f('Ввод_логина', emailfb, 10)
    self.driver.find_element_by_xpath('.//input[@class="oauth_form_input dark"]').send_keys(emailfb)
    time.sleep(4)
    self.page.send_f('Ввод_пароля_VK', passfb, 11)
    time.sleep(4)
    self.page.click_f('Клик_Вход_VK', 12)
    time.sleep(10)

    #self.driver.refresh() # Обновление страницы
    self.prof.click_f('Клик_значок_пользователя', 13)
    
    time.sleep(5)
    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 15)
    resic = str(self.result.find_link("div", "profile-menu__name __username"))    # Проверка авторизации пользователя
    assert ('ТестТест') in resic  # ТестТест - проверочное словосочетание надписи
    self.page.loger_info('Авторизация зарегистрированного на ВК пользователя ТестТест подтверждена')
    self.prof.click_f('Клик_Выйти', 14)
    time.sleep(3)

    self.page.click_f('Клик_Вход', 15)
    time.sleep(1)
    self.page.click_f('Клик_Вход_через_OK', 16)
    time.sleep(4)
    self.page.send_f('Ввод_логина_OK', emailfb, 17)
    time.sleep(4)
    self.page.send_f('Ввод_пароля_OK', passok, 18)
    time.sleep(4)
    self.driver.find_element_by_xpath('.//span[@class="irc-vis"]').click() # Клик по чекбоксу запомнить меня
    time.sleep(4)
    self.page.click_f('Клик_Вход_ОК', 19)
    time.sleep(10)

    #self.driver.refresh() # Обновление страницы
    time.sleep(2)
    self.prof.click_f('Клик_значок_пользователя', 20)
    # self.prof.click_f('Клик_значок_нового_пользователя', 20)
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 15)
    resic = str(self.result.find_link("div", "profile-menu__name __username"))  # Проверка авторизации пользователя
    assert ('Тест Тест') in resic  # ТестТест - проверочное словосочетание надписи
    self.page.loger_info('Авторизация зарегистрированного на ОК пользователя ТестТест подтверждена')
    time.sleep(1)
    self.prof.click_f('Клик_Выйти', 21)
    time.sleep(4)

    self.page.click_f('Клик_Вход', 22)
    time.sleep(2)
    self.page.click_f('Клик_Вход_через_G', 23)
    time.sleep(4)
    self.page.send_f('Ввод_логин_Google', emailgo, 24)
    time.sleep(4)
    self.page.click_f('Клик_1_Далее_Google', 25)
    time.sleep(4)
    self.page.send_f('Ввод_пароль_Google', passgo, 26)
    time.sleep(4)
    self.page.click_f('Клик_кнопки_Далее_Google', 27)
    time.sleep(10)

    #self.driver.refresh() # Обновление страницы
    
    self.prof.click_f('Клик_значок_пользователя', 28)
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 10)
    resic = str(self.result.find_link("div", "profile-menu__name __username"))  # Проверка авторизации пользователя
    assert ('Тест Тест') in resic  # Тест Тест - проверочное словосочетание надписи
    self.page.loger_info('Авторизация зарегистрированного на Google пользователя ТестТест подтверждена')
    time.sleep(1)
    self.prof.click_f('Клик_Выйти', 29)
    time.sleep(3)

    self.page.click_f('Клик_Вход', 30)
    time.sleep(2)
    self.page.click_f('Клик_Вход_через_Mailru', 31)
    time.sleep(4)
    self.page.send_f('Ввод_логин_Mailru', emailru, 32)
    time.sleep(4)
    self.page.send_f('Ввод_пароля_Mailru', passok, 33)
    time.sleep(4)
    self.page.click_f('Клик_Войти_и_разрешить_Mailru', 34)
    time.sleep(10)

    #self.driver.refresh() # Обновление страницы
    time.sleep(2)
    self.prof.click_f('Клик_значок_нового_пользователя', 35)
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 25)  # Проверка авторизации пользователя
    resic = str(self.result.find_link("div", "profile-menu__name __username"))
    time.sleep(1)
    assert ('Имя Фамилия') in resic   # Имя Фамилия - проверочное словосочетание надписи
    self.page.loger_info('Авторизация зарегистрированного на mail.ru пользователя ТестТест подтверждена')
    time.sleep(1)
    self.prof.click_f('Клик_Выйти', 36)
    time.sleep(1)
    self.driver.quit()