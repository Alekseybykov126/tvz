from .page import * 

def case_3_6(self, full_screen):

    email = 'tvzavrtest.test@mail.ru'
    passw = 'Test315492'
    name_user = 'Алексей'

    self.driver.get("https://www.tvzavr.ru/")                   
    self.page.loger('\n Запуск Тест кейс № 3_6 tvweb_new-3_6: Проверка кнопки "Возникла проблема?" в карточке фильма \n')

    time.sleep(3)
    self.page.loger('Шаг 1. Переход в карточку фильма')
    self.driver.find_element_by_xpath('.//a[@class="card card_clip"]').click()
    time.sleep(2)

    self.page.loger('Шаг 2. Клик на кнопку "Возникла проблема?"')
    self.driver.find_element_by_xpath('.//div[@class="clip__feedback"]').click()
    time.sleep(5)

    self.driver.find_element_by_xpath('.//div[@class="clip__feedback"]').click()
    self.page.waitForElementVisible('.//div[@class="modal__content feedback js-modal-content modal__content_open"]', 10)    


    self.driver.find_element_by_xpath('.//input[@class="feedback__name textbox"]').click()

    # self.page.waitForElementVisible('.//div[@class="modal__content feedback js-modal-content modal__content_open"]', 10) # Появление окна "Как мы можем вам помочь?"
    # res_txt = str(self.result.find_all_link("div", "modal__content feedback js-modal-content modal__content_open"))
    # assert('Как мы можем вам помочь?') in res_txt
    # self.page.loger('Появление окна "Как мы можем вам помочь?" подтверждено')
    # time.sleep(2)

    self.page.loger('Шаг 3. Заполнение полей окна обратной связи')
    time.sleep(1)
    self.page.send_f('feedback_имя_пользователя', name_user, 4)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@id="feedback-email"]').send_keys(email)
        
    #self.page.send_f('feedback_e_mail_пользователя', email, 5)
    time.sleep(2)
    
    self.page.send_f('feedback_сообщение_пользователя', 'Автотестирование работы обратной связи WEB tvzavr.ru', 6)
    time.sleep(7)
    
    self.page.click_f('Клик_Отправить_сообщение_обратная связь', 7)
    time.sleep(3)
    
    self.driver.execute_script("window.open('','_blank');") # открытие пустой страницы
    time.sleep(5)

    self.driver.switch_to.window(self.driver.window_handles[1])  # Переключение на вторую страницу
    time.sleep(2)

    self.driver.get("http://rm.tvzavr.ru/projects/helpdesk/issues")   # Переход в РэдМайн
    self.driver.implicitly_wait(10)
    time.sleep(1)
    self.driver.find_element_by_name('button').click()
    self.page.loger('Шаг 8. Переход в службу поддержки подтверждён')
    time.sleep(3)

    self.page.login_google('bykov.a@tvzavr.ru', 'tmW9HZvaksgc')
    self.page.loger('Шаг 9. Введены данные для входа')
    time.sleep(5)

    self.page.waitForElementClickable('.//table[@class="list issues odd-even sort-by-id sort-desc"]', 10)  # Поиск отправленного письма на странице службы поддержки
    res_txt = str(self.result.find_all_link("table", "list issues odd-even sort-by-id sort-desc"))
    assert ('Сообщение пользователя tvzavrtest.test@mail.ru  email:tvzavrtest.test@mail.ru') in res_txt
    self.page.loger('Шаг 10. Отправленное письмо найдено на странице службы поддержки')
    time.sleep(3)

    self.driver.close()
    time.sleep(2)
    self.driver.switch_to.window(self.driver.window_handles[-1])  # Переключение на предыдущую вкладку
    time.sleep(2)
    self.page.loger('Подтверждена отправка сообщения в тех.поддержку из карточки фильма')
    time.sleep(2)

    self.driver.quit() 