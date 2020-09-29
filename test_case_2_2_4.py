from .page import *

time.sleep(2)
def case_2_2_4(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_2_4 tvweb_new-2_2_4: Проверка фильтров поиска на странице Бесплатно(Года, Жанры, Страны)')
    
    time.sleep(1)
    self.page.click_f('Клик_Бесплатно', 17)
    time.sleep(3)
    self.page.click_f('Клик_Сериалы_в_каталоге', 18)
    time.sleep(3)

    self.page.click_f('Клик_Годы_выпуска', 19)   
    time.sleep(1)
    pyautogui.moveTo(442, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1000, 599, 2, button='left') #конечные координаты
    time.sleep(1)
    pyautogui.moveTo(1462, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1457, 599, 2, button='left') #конечные координаты
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 20)
    time.sleep(2)

    self.page.click_f('Клик_Жанры', 21)
    time.sleep(1)
    self.page.click_f('Клик_приключения_жанр', 22)
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 23)
    time.sleep(3)       
    
    self.page.click_f('Клик_страны', 24)
    time.sleep(1)
    self.page.click_f('Клик_Турция', 25)
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 26)
    time.sleep(2)   
    self.page.click_f('Клик_постер_первого_фильма', 27)
    time.sleep(3)

    year = self.driver.find_element_by_xpath("//a[@class='js-clip-year']") # проверка года 
    year = year.get_attribute('innerHTML')
    self.page.loger('Год сериала: ' + year)
    time.sleep(1)
    year = int(year)

    if 1964 <= year <= 2018:
        self.page.loger('Год сериала соответствует фильтру')
    else:
        self.page.loger('Год сериала не соответствует фильтру')
        assert()
    
    self.card.click_f('Клик_на_вкладку_описание', 28)  # Переключение на описание, чтобы было видно страну
    time.sleep(2)
    self.page.waitForElementVisible('.//a[@class="js-clip-info-country"]', 10) # проверяем наличие страны  Турция в карточке фильма
    time.sleep(1)
    resic = str(self.result.find_all_link("a", "js-clip-info-country"))
    assert ('Турция') in resic  # проверочное словосочетание надписи
    self.page.loger_info('Наличие страны "Турция" в карточке фильма подтверждено')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="clip-info__value"]', 10)  # проверяем наличие жанра Приключения в карточке фильма
    resic = str(self.result.find_all_link("div", "clip-info__value"))
    assert ('Приключения') in resic  # проверочное словосочетание надписи
    self.page.loger_info('Наличие жанра "Приключения" в карточке фильма подтверждено')
    time.sleep(2)

    self.driver.quit()