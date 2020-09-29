from .page import *

def case_3_5(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 3_5 tvweb_new-3_5: Проверка переключения серий и сезонов сериала \n')
    time.sleep(1)    

    self.page.send_f('Ввод_2_в_строку_поиска', 'Воскресший Эртугрул', 1)
    time.sleep(4)
    
    self.prof.click_f('Клик_поиска_Лупа', 2)
    time.sleep(2)

    self.page.waitForElementVisible('.//a[@href="/film/voskresshii-ertugrul/"]', 30)
    
    self.driver.find_element_by_xpath('.//a[@href="/film/voskresshii-ertugrul/"]').click()
    self.page.loger('Шаг 3. Клик постер сериала Воскресший Эртугрул')   # идет воспроизведение сериала
    time.sleep(5)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 10)   # Проверка названия сериала в заголовке
    res_txt = str(self.result.find_link("h1", "clip__name heading-1"))  
    assert ('Воскресший Эртугрул') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Наличие названия в заголовке подтверждено')
    time.sleep(2)

    target = self.driver.find_element_by_xpath('.//button[@class="clip__action clip-share__button"]')  # элемент Поделиться  
    target.location_once_scrolled_into_view  # скролл до элемента target
    self.page.loger('Шаг 4. прокрутил до Поделиться')
    time.sleep(2) 
    
    self.driver.find_element_by_xpath('.//a[@data-target="clip-series"]').click() # Клик на серии
    self.page.waitForElementVisible('.//a[@data-cid="42223"]', 30)

    self.driver.find_element_by_xpath('.//a[@data-cid="42223"]').click()  # клик на 1-ю серию
    self.page.loger('Шаг 5. Клик первой серии произведен')
    time.sleep(5)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 10)   # Проверка появления Серия 1 в заголовке
    res_txt = str(self.result.find_link("h1", "clip__name heading-1"))  
    assert ('Серия 1') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 6. наличие Серия 1 подтверждено')
    time.sleep(2)

    target = self.driver.find_element_by_xpath('.//button[@class="clip__action clip-share__button"]')  # элемент Поделиться  
    target.location_once_scrolled_into_view  # скролл до элемента target
    self.page.loger('Шаг 7. прокрутил до Поделиться')
    time.sleep(2) 
    
    self.driver.find_element_by_xpath('.//a[@data-target="clip-series"]').click() # Клик на серии
    self.page.waitForElementVisible('.//a[@data-cid="42223"]', 30)

    self.driver.find_element_by_xpath('.//a[@data-cid="42257"]').click()  # Серия 35
    self.page.loger('Шаг 8. Переключение на 35 серию')   
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 30)   # Проверка появления Серия 35 в заголовке
    res_txt = str(self.result.find_link("h1", "clip__name heading-1"))  
    assert ('Серия 35') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 10. наличие Серия 35 в заголовке подтверждено')
    time.sleep(2)

    target = self.driver.find_element_by_xpath('.//button[@class="clip__action clip-share__button"]')  # элемент Поделиться  
    target.location_once_scrolled_into_view  # скролл до элемента target
    self.page.loger('Шаг 11. прокрутил до Поделиться')
    time.sleep(2) 
    
    self.driver.find_element_by_xpath('.//a[@data-target="clip-series"]').click() # Клик на серии
    self.page.waitForElementVisible('.//a[@data-cid="42223"]', 30)

    target = self.driver.find_element_by_xpath('.//a[@data-cid="42283"]')  # скролл до серии 61
    target.location_once_scrolled_into_view  # скролл до элемента target
    self.page.loger('Шаг 11. прокрутил до 61 серии')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@data-cid="42298"]').click()  # Серия 76
    self.page.loger('Шаг 12. Переключение на серию 76 успешно')
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 30)   # Проверка появления Серия 40 в заголовке
    res_txt = str(self.result.find_link("h1", "clip__name heading-1"))  
    assert ('Серия 76') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 14. наличие Серия 76 в заголовке подтверждено')
    time.sleep(2)

    
    target = self.driver.find_element_by_xpath('.//button[@class="clip__action clip-share__button"]')  # элемент Поделиться  
    target.location_once_scrolled_into_view  # скролл до элемента target
    self.page.loger('Шаг 15. прокрутил до Поделиться')
    time.sleep(2) 
    
    self.driver.find_element_by_xpath('.//a[@data-target="clip-series"]').click() # Клик на серии
    self.page.waitForElementVisible('.//a[@data-cid="42223"]', 30)

    self.driver.find_element_by_xpath('.//button[@data-target="42299"][contains(., "Сезон 2")]').click()  # Сезон 2
    self.page.loger('Шаг 16. Переключение на сезон 2 успешно')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@data-cid="42300"]').click()  # клик на 1-ю серию
    self.page.loger('Шаг 17. клик на 1-ю серию')
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 30)   # Проверка появления Серия 40 в заголовке
    res_txt = str(self.result.find_link("h1", "clip__name heading-1"))  
    assert ('Серия 1') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 18. наличие Серия 1 в заголовке подтверждено')
    time.sleep(1)      

    target = self.driver.find_element_by_xpath('.//button[@class="clip__action clip-share__button"]')  # элемент Поделиться  
    target.location_once_scrolled_into_view  # скролл до элемента target
    self.page.loger('Шаг 19. прокрутил до Поделиться')
    time.sleep(2) 
    
    self.driver.find_element_by_xpath('.//a[@data-target="clip-series"]').click() # Клик на серии
    time.sleep(2)
    self.driver.find_element_by_xpath('.//button[@data-target="42299"][contains(., "Сезон 2")]').click()  # Сезон 2
    self.page.loger('Шаг 20. Переключение на сезон 2 успешно')
    #self.page.waitForElementVisible('.//a[@data-cid="42223"]', 30)

    self.driver.find_element_by_xpath('.//a[@data-cid="42313"]').click()  # клик на 14-ю серию
    self.page.loger('Шаг 21. клик на 14-ю серию')
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"]', 30)   # Проверка появления Серия 40 в заголовке
    res_txt = str(self.result.find_link("h1", "clip__name heading-1"))  
    assert ('Серия 14') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 22. наличие Серия 14 в заголовке подтверждено')
    time.sleep(1)
    self.driver.quit() 