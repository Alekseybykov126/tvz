from .page import *

time.sleep(2)
def case_2_3_4(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_3_4 tvweb_new-2_3_4: Проверка фильтров поиска на странице Новинки(Года, Жанры, Страны)')

    time.sleep(1)
    self.page.click_f('Клик_Новинки', 17)
    time.sleep(3)
    self.page.click_f('Клик_Сериалы_в_каталоге', 18)
    time.sleep(3)

    self.page.click_f('Клик_Годы_выпуска', 19)   
    time.sleep(1)
    pyautogui.moveTo(442, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1420, 599, 3, button='left') #конечные координаты
    time.sleep(1)
    pyautogui.moveTo(1459, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1454, 599, 1, button='left') #конечные координаты
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 20)
    time.sleep(2)

    self.page.click_f('Клик_Жанры', 21)
    time.sleep(1)
    self.page.click_f('Клик_Детектив_жанр', 22)
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 23)
    time.sleep(3)       
    
    self.page.click_f('Клик_страны', 24)
    time.sleep(1)
    self.page.click_f('Клик_Россия', 25)
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 26)
    time.sleep(2)   
    self.page.click_f('Клик_постер_первого_фильма', 27)
    time.sleep(3)

    res_txt = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Название фильма: ' + res_txt.strip())
    time.sleep(1)  

    year = self.driver.find_element_by_xpath("//a[@class='js-clip-year']") # проверка года 
    year = year.get_attribute('innerHTML')
    self.page.loger('Год сериала: ' + year)
    time.sleep(1)
    year = int(year)

    if 2016 <= year <= 2018:
        self.page.loger('Год сериала соответствует фильтру')
    else:
        self.page.loger('Год сериала не соответствует фильтру')
        assert()

    self.card.click_f('Клик_на_вкладку_описание', 28)  # Переключение на описание, чтобы было видно страну
    time.sleep(2)
    self.page.waitForElementVisible('.//a[@class="js-clip-info-country"]', 10) # проверяем наличие страны  Южная Корея в карточке фильма
    time.sleep(1)
    resic = str(self.result.find_all_link("a", "js-clip-info-country"))
    assert ('Россия') in resic  # проверочное словосочетание надписи
    self.page.loger_info('Наличие страны "Россия" в карточке фильма подтверждено')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="clip-info__value"]', 10)  # проверяем наличие жанра азиатский в карточке фильма
    resic = str(self.result.find_all_link("div", "clip-info__value"))
    assert ('Детектив') in resic  # проверочное словосочетание надписи
    self.page.loger_info('Наличие жанра "Детектив" в карточке фильма подтверждено')
    time.sleep(1)

    self.driver.quit()