from Regress_web.page import *

time.sleep(2)
def case_4(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 4 tvweb_new-4: Проверка фильтров поиска на странице Каталог')
    
    
    
    #### это не снимать!! year_1 = self.driver.find_element_by_xpath("//button[@data-source-id='years-from']")   эти две функции сохраняют значение фильтра
    # year_1 = year_1.get_attribute('innerHTML')
    # self.page.loger(year_1)
    # time.sleep(2)

    # year_2 = self.driver.find_element_by_xpath("//button[@data-source-id='years-to']")     эти две функции сохраняют значение фильтра
    # year_2 = year_2.get_attribute('innerHTML')
    # self.page.loger(year_2)
    # year_1 = int(year_1)
    # year_2 = int(year_2)
    #### это не снимать!! self.page.loger(year_1, year_2)