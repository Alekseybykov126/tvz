from .page import *

time.sleep(2)
def case_3_4(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 3_4  tvweb_new-3_4: Проигрывание купленных фильмов \n')
    emailt = 'testaleh126@mail.ru'
    passw = '1234567'

    time.sleep(2)
    self.page.click_f('Клик_Вход', 1)
    time.sleep(2)

    #self.page.send_f('Ввод_логина_вход', emailt, 2)
    self.driver.find_element_by_xpath('.//input[@class="authorization__login textbox"]').send_keys(emailt)
    time.sleep(2)

    #self.page.send_f('Ввод_пароля_вход', passw, 3)
    self.driver.find_element_by_xpath('.//input[@class="authorization__password textbox"]').send_keys(passw)
    time.sleep(2)
    
    self.page.click_f('Клик_Войти_auth', 4)
    time.sleep(3)
        
    self.prof.click_f('Клик_значок_пользователя', 5)
    time.sleep(1)
    self.prof.click_f('Клик_мои_фильмы', 6)
    time.sleep(3)
    
    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2"]', 10)  # Проверка перехода"
    time.sleep(1)
    resic = str(self.result.find_link("div", "selection__heading heading-2"))
    assert ('Купленные фильмы') in resic # проверочное словосочетание надписи
    self.page.loger('Подтвержден переход в кабинет и наличие купленных фильмов')
    time.sleep(2)

    self.page.loger('Шаг 7. Переход в карточку фильма')
    b = random.randint(1, 3)
    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[b].click() # Рандомный фильм
    time.sleep(3)

    movie_name = (self.result.find_link("h1", "clip__name heading-1"))  # Название заголовка в карточке фильма
    movie_text = movie_name.text
    self.page.loger('Название фильма: ' + movie_name.text)
    time.sleep(2)
    
    self.card.click_f('Клик_Play', 8)
    time.sleep(10)

    pyautogui.moveTo(1300, 460, duration = 1)
    pyautogui.moveTo(1000, 600, duration = 1)
    
    self.card.click_f('Клик_пауза', 9)
    time.sleep(2)

    self.page.loger('Шаг 10. Проверка автоматического воспроизведения фильма')
    self.page.waitForElementVisible('.//span[@class="tvz-time_label tvz-timerow-current_time"]', 11) #получение времени остановки
    resic = self.result.find_link("span", "tvz-time_label tvz-timerow-current_time").text
    self.page.loger('Воспроизведение фильма. Время остановки: ' + resic)
    time.sleep(1)

    if resic == '00:00:00':
        assert(), "Фильм не воспроизвелся автоматически" 
    else:
        self.page.loger('Автоматическое воспроизведение фильма подтверждено')
    
    self.prof.click_f('Клик_значок_пользователя', 11)
    time.sleep(1)
    self.prof.click_f('Клик_мои_фильмы', 12)
    time.sleep(3)

    self.prof.click_f('Клик_значок_пользователя', 11)
    time.sleep(1)
    self.prof.click_f('Клик_Выйти', 12)
    time.sleep(1)

    self.driver.quit()    