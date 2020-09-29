from Regress_web.page import *

def case_00(self, full_screen):
    time.sleep(1)

    self.page.loger('\n Запуск Тест кейс № 00 tvweb_new-00: Проигрывание фильмов циклом \n')

    self.page.click_f('Клик_Бесплатно', 1)
    time.sleep(5)

    self.page.loger('Шаг 2. Переход в карточку фильма')
    b = random.randint(1, 23)
    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[b].click() # Клик на рандомный фильм
    time.sleep(2)

    rec_sic = (self.result.find_link("h1", "clip__name heading-1")) # копируем название первого фильма в списке бесплатных фильмов
    rec_text = rec_sic.text
    self.page.loger('Название фильма: ' + rec_sic.text)
    time.sleep(2)

    target = self.driver.find_element_by_xpath("//h1[@class='clip__name heading-1']") # скролл до заголовка страницы
    target.location_once_scrolled_into_view # скролл
    time.sleep(95)
        
    pyautogui.moveTo(1300, 460, duration = 2)   # двигаем, чтобы показались кнопки плеера
    pyautogui.moveTo(1000, 600, duration = 2)
    time1 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]') # запоминание первое значение времени
    time1text = time1.text
    self.page.loger(time1text)
    time.sleep(5)

    pyautogui.moveTo(1300, 460, duration = 2)   # двигаем, чтобы показались кнопки плеера
    pyautogui.moveTo(1000, 600, duration = 2)
    time2 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]') # запоминание второго значения времени
    time2text = time1.text
    self.page.loger(time2text)
    time.sleep(2)

    if time1text != time2text:
        self.page.loger('Фильм начал воспроизведение')
    else:
        assert(), "Фильм не воспроизвелся"
    