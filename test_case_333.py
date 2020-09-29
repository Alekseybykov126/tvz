print('dddddd')



# from Regress_web.page import * 
# def case_333(self, full_screen):

#     self.page.loger('\n Запуск Тест кейс № 333 tvweb_new-333: Эксперимент \n')

#     self.page.click_f('Клик_Каталог', 6)
#     time.sleep(3)
#     self.page.click_f('Клик_Фильмы_в_каталоге', 7)
#     time.sleep(2)    
#     self.page.click_f('Клик_страны', 8)
#     time.sleep(1)
    
#     b = random.randint(0, 93)
#     self.driver.find_elements_by_xpath('.//li[@data-filter-type="countries"]')[b].click()
#     self.page.click_f('Клик_применить_фильтр', 4)  

#     country1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_countries"]') # Страна в выборке
#     country1 = country1.get_attribute('innerHTML')
#     text = country1
#     self.page.loger('Выбранная страна: ' + country1)

#     m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильмов
#     print(len(m))  

#     while (len(m)) < 1:
#         self.driver.find_element_by_xpath('.//button[@class="filter__reset js-filter-reset"]').click() # Клик сбросить
#         time.sleep(3)
#         self.page.click_f('Клик_Каталог', 6)
#         time.sleep(3)
        
#         self.page.click_f('Клик_страны', 8)
#         time.sleep(1)
#         b = random.randint(0, 93)
#         self.driver.find_elements_by_xpath('.//li[@data-filter-type="countries"]')[b].click()
#         time.sleep(2)
#         self.page.click_f('Клик_применить_фильтр', 4)

#         country1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_countries"]') # Страна в выборке
#         country1 = country1.get_attribute('innerHTML')
#         text = country1
#         self.page.loger('Выбранная страна: ' + country1)
        
#         m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильвом
#         print(len(m))

#     p = random.randint(0, (len(m) - 1))
#     self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[p].click()
#     time.sleep(3)

#     country3 = self.driver.find_element_by_xpath('.//div[@class="clip__countries"]')
#     country3text = country3.text
#     self.page.loger('Страны в карточке фильма: ' + country3text)

#     assert (country1) in country3text  # проверочное словосочетание надписи
#     self.page.loger_info('Наличие страны ' + country1 + ' в карточке фильма подтверждено')
#     time.sleep(1)

#     self.driver.quit()
       