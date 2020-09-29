from .page import * 

time.sleep(1)
def case_6_5(self, full_screen):

    self.page.loger('\n Запуск Тест кейс № 6_5 tvweb_new-6_5: Проверка добавления и удаления комментария \n')

    emailt = 'ttvzavr126@mail.ru'
    passw = '111111'

    self.page.click_f('Клик_Вход', 1)
    time.sleep(1)
    #self.page.send_f('Ввод_логина_вход', emailt, 2)
    self.driver.find_element_by_xpath('.//input[@class="authorization__login textbox"]').send_keys(emailt)
    time.sleep(2)

    #self.page.send_f('Ввод_пароля_вход', passw, 3)
    self.driver.find_element_by_xpath('.//input[@class="authorization__password textbox"]').send_keys(passw)
    time.sleep(2)

    self.page.click_f('Клик_Войти_auth', 2)
    time.sleep(5)

    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2"][contains(., "Рекомендуем")]', 10)
    target = self.driver.find_element_by_xpath('.//div[@class="selection__heading heading-2"][contains(., "Рекомендуем")]') # скролл до заголовка с названием фильма
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@href="/catalog/besplatnye-filmy/"][contains(., "Смотреть все")]').click() # Клик
    time.sleep(3)

    self.driver.find_element_by_xpath('.//a[@class="card card_clip"]').click()
    time.sleep(4)

    target = self.driver.find_element_by_xpath('.//button[@data-modal="feedback"]') # скролл до заголовка с названием фильма
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.card.click_f('Клик_на_вкладку_Отзывы ', 3)
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//textarea[@class="clip-comments__field textbox"]').send_keys('Суперр!')
    time.sleep(3)
    
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@id="clip-comments-send"]').click()
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="clip-comments__list"]', 10) # Поиск блока с комментариями
    res_txt = str(self.result.find_all_link("div", "clip-comments__list"))
    assert('Алексей') in res_txt
    assert('Суперр!') in res_txt
    self.page.loger('Комментарий добавлен')
    time.sleep(2)

    self.page.delete_comments('ttvzavr126@mail.ru') # Удаление комментариев
    self.page.loger('Комментарии пользователя "ttvzavr126@mail.ru" удалены в админке')
    time.sleep(3)

    self.driver.close() # Закрыть вкладку
    self.driver.switch_to.window(self.driver.window_handles[-1]) # Переключиться на предыдущую вкладку
    time.sleep(3)

    self.driver.refresh()
    time.sleep(5)

    self.page.waitForElementVisible('.//div[@class="clip-comments__list"]', 10) # Поиск блока с комментариями
    res_txt = str(self.result.find_all_link("div", "clip-comments__list"))
    assert('Fktrctq') not in res_txt
    assert('Суперр!') not in res_txt
    self.page.loger('Комментарий удален из отзывов')
    time.sleep(2)

    self.driver.quit()