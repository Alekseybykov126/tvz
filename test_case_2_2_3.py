from .page import *

time.sleep(2)
def case_2_2_3(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_2_3 tvweb_new-2_2_3: Проверка фильтров поиска на странице Бесплатно(Годы)')

    time.sleep(1)
    self.page.click_f('Клик_Бесплатно', 6)
    time.sleep(3)

    self.page.click_f('Клик_Мультфильмы_в_каталоге', 13)
    time.sleep(3)
    self.page.click_f('Клик_Годы_выпуска', 14)   
    time.sleep(1)

    pyautogui.moveTo(442, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(850, 599, 2, button='left') #конечные координаты
    time.sleep(1)
    pyautogui.moveTo(1462, 599, duration = 1) #начальные координаты
    pyautogui.dragTo(1200, 599, 2, button='left') #конечные координаты
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 15)
    time.sleep(2)

    self.page.click_f('Клик_постер_первого_фильма', 16)
    year = self.driver.find_element_by_xpath("//a[@class='js-clip-year']") # проверка года 
    year = year.get_attribute('innerHTML')
    self.page.loger('Год мультфильма: ' + year)
    time.sleep(1)
    year = int(year)

    if 1946 <= year <= 1988:
        self.page.loger('Год мультфильма соответствует фильтру')
    else:
        self.page.loger('Год мультфильма не соответствует фильтру')
        assert()
    time.sleep(2)

    self.driver.quit()