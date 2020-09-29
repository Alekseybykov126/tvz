from Regress_web.page import * 
def case_222(self, full_screen):

    self.page.loger('\n Запуск Тест кейс № 222 tvweb_new-222: Эксперимент \n')

    self.driver.find_element_by_xpath('.//div[@class="owl-item active"]').click()
    time.sleep(2)

    # res_txt = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    # self.page.loger('Название фильма: ' + res_txt.strip())
    # time.sleep(2)

    # target = self.driver.find_element_by_xpath('.//div[@class="clip-info__label"]') # скролл до заголовка с названием фильма
    # target.location_once_scrolled_into_view # скролл
    # time.sleep(2)

    # self.driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)

    # time.sleep(2)

    # self.driver.find_element_by_xpath('.//li[@class="tabs__item js-tabs-item"]').click()
    # time.sleep(2)
    # self.driver.find_elements_by_xpath('.//li[@class="tabs__item js-tabs-item"]')[1].click()
    # time.sleep(2)

    # time.sleep(2)

    # self.driver.find_element_by_xpath('.//div[@class="series-card__poster"]').click()
    # time.sleep(5)

    # pyautogui.moveTo(1319, 500, duration = 4)  # двигаем, чтобы показались кнопки плеера
    # self.page.waitForElementVisible('.//div[@class="tvz-controls_dock tvz-controls_dock-movie tvz-panel"]', 3)
    # self.card.click_f('Клик_пауза', 8)
    # time.sleep(2)

    # self.driver.find_element_by_xpath('.//a[@href="/genres/2019/"]').click()
    # time.sleep(3)

    # year = str(self.result.find_link("h1", "page__heading superheading-1"))    
    # assert ('2019') in year

    # b = random.randint(1, 5)
    # self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[b].click()
    # time.sleep(3)

    # name_of_movie = str(self.driver.find_element_by_xpath('.//h1[@class="clip__name heading-1"]').text)
    # self.page.loger('Название фильма: ' + name_of_movie)
    # time.sleep(2)

    # self.driver.back()
    # time.sleep(2)

    # self.driver.find_elements_by_xpath('.//span[@class="toggle__label"]')[0].click()
    # time.sleep(2)
    # self.driver.find_elements_by_xpath('.//span[@class="toggle__label"]')[1].click()
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header__login"]').click()
    time.sleep(2)

    self.driver.find_element_by_xpath('.//body[@class="page page_unauthorized page_modal-open"]').send_keys(Keys.ESCAPE)
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@href="/genres/"]').click()
    time.sleep(3)

    





    # self.driver.find_element_by_xpath('.//a[@href="/novinki/"]').click()
    # self.driver.find_element_by_xpath('.//a[@href="/subscription/"]').click()
    # self.driver.find_element_by_xpath('.//a[@href="/besplatno/"]').click()
    # self.driver.find_element_by_xpath('.//a[@href="/topics/"]').click()
    # self.driver.find_element_by_xpath('.//a[@href="/genres/"]').click()
    # self.driver.find_element_by_xpath('.//a[@href="/kids/"]').click()
    # self.driver.find_element_by_xpath('.//a[@href="/specprojects/"]').click()

    

    
   

    #self.driver.quit()







    
    
    
