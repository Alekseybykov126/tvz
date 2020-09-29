from Regress_web.page import * 
def case_25(self, full_screen):

    self.page.loger('\n Запуск Тест кейс № 25 tvweb_new-25: Эксперимент \n')

    time.sleep(1)
        
    # self.page.click_f('Клик_Каталог', 1)
    # time.sleep(3)

    # self.page.click_f('Клик_Жанры', 2)
    # time.sleep(1)

    # b = random.randint(0, 44)

    # self.driver.find_elements_by_xpath('.//li[@data-filter-type="genres"]')[b].click()
    # time.sleep(2)
    # self.page.click_f('Клик_применить_фильтр', 4)

    # genre1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_genres"]')
    # genre1text = genre1.text
    # self.page.loger('Выбранный жанр: ' + genre1text)

    # self.page.click_f('Клик_постер_первого_фильма', 5)
    # time.sleep(3)

    # genre2 = self.driver.find_element_by_xpath('.//div[@class="clip__genres"]')
    # genre2text = genre2.text
    # self.page.loger('Жанры в карточке фильма: ' + genre2text)

    # assert (genre1text) in genre2text  # проверочное словосочетание надписи
    # self.page.loger_info('Наличие жанра ' + genre1text + ' в карточке фильма подтверждено')
    # time.sleep(1)





    self.page.click_f('Клик_Каталог', 6)
    time.sleep(3)
    #self.page.click_f('Клик_Фильмы_в_каталоге', 7)
    #time.sleep(3)
    self.page.click_f('Клик_страны', 8)
    time.sleep(1)

    b = random.randint(0, 93)

    self.driver.find_elements_by_xpath('.//li[@data-filter-type="countries"]')[b].click()  # рандомный выбор фильма
    #self.driver.find_element_by_xpath('.//li[@data-filter-id="23390"]').click() # Иран  
    #self.driver.find_element_by_xpath('.//li[@data-filter-id="515"]').click() # США
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 4)

    
    m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')
    print(len(m))

    country1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_countries"]') # Страна в выборке
    country1 = country1.get_attribute('innerHTML')
    text = country1
    self.page.loger('Выбранная страна: ' + country1)

    try:        
        self.page.waitForElementClickable('.//a[@class="card card_clip"]', 5) 
        self.page.loger('У страны ' + country1 + ' есть фильмы')
        time.sleep(1)
        #self.page.click_f('Клик_постер_первого_фильма', 5)
        p = random.randint(0, (len(m) - 1))
        self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[p].click()
        time.sleep(3)

        country3 = self.driver.find_element_by_xpath('.//div[@class="clip__countries"]')
        country3text = country3.text
        self.page.loger('Страны в карточке фильма: ' + country3text)

        assert (country1) in country3text  # проверочное словосочетание надписи
        self.page.loger_info('Наличие страны ' + country1 + ' в карточке фильма подтверждено')
        time.sleep(1)
        
    except:
        self.page.loger('У страны ' + country1 + ' нет фильмов')
        time.sleep(1)

        self.driver.find_element_by_xpath('.//button[@class="filter__reset js-filter-reset"]').click() # Клик сбросить
        time.sleep(3)

        self.page.click_f('Клик_Каталог', 6)
        time.sleep(3)
        self.page.click_f('Клик_Фильмы_в_каталоге', 7)
        time.sleep(3)


        self.page.click_f('Клик_страны', 8)
        time.sleep(1)

        t = random.randint(0, 93)

        self.driver.find_elements_by_xpath('.//li[@data-filter-type="countries"]')[t].click()
        time.sleep(2)
        self.page.click_f('Клик_применить_фильтр', 4)
        
        country5 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_countries"]') # Страна в выборке
        country5 = country5.get_attribute('innerHTML')
        text = country5
        self.page.loger('Выбранная страна: ' + country5)

        self.page.click_f('Клик_постер_первого_фильма', 5)
        time.sleep(3)

        country4 = self.driver.find_element_by_xpath('.//div[@class="clip__countries"]')
        country4text = country4.text
        self.page.loger('Страны в карточке фильма: ' + country4text)

        assert (country5) in country4text  # проверочное словосочетание надписи
        self.page.loger_info('Наличие жанра ' + country5 + ' в карточке фильма подтверждено')
        time.sleep(1)
    
    self.driver.quit()

        