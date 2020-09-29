from .page import *

time.sleep(2)
def case_2_3_7(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_3_7 tvweb_new-2_3_7: Проверка фильтров поиска на странице Новинки(Родительский контроль)')

    time.sleep(1)
    self.page.click_f('Клик_Новинки', 33)
    time.sleep(3)
    self.driver.find_element_by_xpath('.//span[@class="toggle__label"][contains(., "Родительский контроль")]').click()  # клик родительский контроль
    self.page.loger('Поставил галочку на Родительский контроль')
    time.sleep(3)   
    self.page.click_f('Клик_постер_первого_фильма', 34)

    age = self.driver.find_element_by_xpath("//div[@class='clip__age']") # проверка возростного ограничения 
    age = age.get_attribute('innerHTML')
    self.page.loger('Возрастное ограничение в карточке фильма: ' + age)
    time.sleep(1)
    
    if age != '18+':
        self.page.loger('Фильм соответствует фильтру родительский контроль')
    else:
        self.page.loger('Фильм не соответствует фильтру родительский контроль')
        assert()
    time.sleep(2)

    self.driver.quit()