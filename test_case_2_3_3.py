from .page import *

time.sleep(2)
def case_2_3_3(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_3_3 tvweb_new-2_3_3: Проверка фильтров поиска на странице Новинки(Года)')
    
    time.sleep(1)
    self.page.click_f('Клик_Новинки', 12)
    time.sleep(3)
    self.page.click_f('Клик_Мультфильмы_в_каталоге', 13)
    time.sleep(3)
    self.page.click_f('Клик_Годы_выпуска', 14)   
    time.sleep(1)

    pyautogui.moveTo(442, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1420, 599, 3, button='left') #конечные координаты
    time.sleep(1)
    pyautogui.moveTo(1462, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1455, 599, 1, button='left') #конечные координаты
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 15)
    time.sleep(2)

    self.page.click_f('Клик_постер_первого_фильма', 16)

    res_txt = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Название фильма: ' + res_txt.strip())
    time.sleep(1)  

    year = self.driver.find_element_by_xpath("//a[@class='js-clip-year']") # проверка года 
    year = year.get_attribute('innerHTML')
    self.page.loger('Год мультфильма: ' + year)
    time.sleep(1)
    year = int(year)

    if 2016 <= year <= 2018:
        self.page.loger('Год мультфильма соответствует фильтру')
    else:
        self.page.loger('Год мультфильма не соответствует фильтру')
        assert()
    time.sleep(2)

    self.driver.quit()