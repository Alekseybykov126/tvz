from .page import *

time.sleep(3)
def case_3_3(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 3_3   tvweb_new-3_3: Проверка элементов карточки бесплатного фильма, проигрывание и переход по похожим фильмам \n')
           
    self.page.click_f('Клик_Бесплатно', 1)
    time.sleep(2)
    b = random.randint(1, 23)

    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[b].click()
    time.sleep(5)

    res_txt = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Наличие названия фильма: ' + res_txt.strip())
    time.sleep(1)  
    #self.page.click_f('Клик_постер_первого_фильма', 2)
    

    # self.page.waitForElementVisible('.//span[@class="tvz-button_disable_ad tvz-button_disable_ad js-trial-info"]', 10)    
    # res_txt = str(self.result.find_link("span", "tvz-button_disable_ad tvz-button_disable_ad js-trial-info"))  # Проверка наличия кнопки Отключите рекламу за 1 рубль
    # assert ('Отключите рекламу за 1 рубль') in res_txt   # проверочное словосочетание надписи
    # self.page.loger('Наличие кнопки "Отключите рекламу за 1 рубль" подтверждено')        
    # time.sleep(1)

    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2 js-category-title"][contains(., "Похожие фильмы")]', 10) # Проверка наличия похожих фильмов
    res_txt = str(self.result.find_link("div", "selection__heading heading-2 js-category-title"))
    assert ('Похожие фильмы') in res_txt # Проверка наличия Похожих фильмов
    self.page.loger('Шаг 3. Наличие Похожих фильмов подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//a[@class="card card_clip"]').click() # Клик первого фильма в Похожих
    time.sleep(2)

    self.page.loger('Шаг 4. Переход в похожие фильмы')

    res_txt2 = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Наличие названия фильма: ' + res_txt2.strip())
    time.sleep(7)
    
    self.driver.find_element_by_xpath('.//a[@data-target="clip-comments"]').click() # переход в отзывы
    self.card.click_f('Клик_на_вкладку_Отзывы ', 5)
    time.sleep(3)

    self.page.waitForElementVisible('.//*[@id="clip-comments-field"]', 10)
    self.page.loger('Шаг 6. Поле для ввода комментариев найдено')
    time.sleep(1)

    target = self.driver.find_element_by_xpath('.//div[@class="selection__heading heading-2 js-category-title"]')
    target.location_once_scrolled_into_view
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="slider__navigation slider__navigation_next js-slider-navigation js-slider-navigation-next"]').click() #прокручивает похожие фильмы вправо
    self.page.loger('Шаг 7. Прокрутка похожих фильмов')
    time.sleep(5)

    self.driver.find_element_by_xpath('.//div[@class="owl-item active"]').click() # кликает первый фильм в похожих
    time.sleep(3)

    self.page.loger('Шаг 8. Перешел в похожий фильм')
    time.sleep(1)

    res_txt3 = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Наличие названия фильма: ' + res_txt3.strip())
    time.sleep(1)  

    target = self.driver.find_element_by_xpath('.//div[@class="clip__actions"]')
    target.location_once_scrolled_into_view
    time.sleep(1)
    
    try:
        self.driver.find_element_by_xpath('.//a[@data-target="clip-trailers"]')   # переход на вкладку трейлеры
        time.sleep(2)
        self.driver.find_element_by_xpath('.//button[@class="clip-trailers__card series-card"]').click()
        time.sleep(5)
        self.driver.waitForElementVisible('.//span[@class="tvz-time_label tvz-timerow-current_time"]', 10)
        self.page.loger('Трейлер воспроизвелся')
                
    except:
        self.page.loger('Возможно, для этого фильма нет трейлера')
    time.sleep(1)

    try:
        self.card.click_f('Клик_на_вкладку_Награды', 11)
        time.sleep(2)
        self.page.waitForElementVisible('.//div[@class="clip-awards"]', 10)
        res_txt = str(self.result.find_all_link("div", "clip-awards"))
        assert('clip-awards__item') in res_txt
        self.page.loger('Наличие наград подтверждено')
    except:
        self.page.loger('Возможно, у этого фильма нет наград')
    time.sleep(2)

    self.card.click_f('Клик_на_вкладку_описание', 12)
    self.page.waitForElementVisible('.//h2[@class="clip__subheading"]', 10) # Проверка наличия вкладки Описание
    res_txt = str(self.result.find_link("h2", "clip__subheading"))
    assert ('Описание') in res_txt #- проверочное словосочетание
    self.page.loger('Шаг 13. Переход на вкладку Описание подтверждено')

    self.page.waitForElementVisible('.//div[@class="clip-info"]', 10) # Проверка наличия информации о фильме
    res_txt = str(self.result.find_link("div", "clip-info"))
    assert ('Жанр:') in res_txt # Проверка наличия жанра
    self.page.loger('Шаг 14. Наличие жанра подтверждено')

    assert ('Режиссер:') in res_txt # Проверка наличия Режиссера
    self.page.loger('Шаг 15. Наличие режиссера подтверждено')

    assert ('В ролях:') in res_txt # Проверка наличия В ролях
    self.page.loger('Шаг 16. Наличие в ролях подтверждено')
    
    res_min = str(self.result.find_link("div", "clip-info__duration").text)  # Проверка наличия продолжительности фильма
    if 'минут ' in res_min:        # проверочное словосочетание надписи
        self.page.loger_info('Наличие продолжительности фильма' + res_min + ' подтверждено')
    elif 'час' or 'часа' in res_min:
        self.page.loger_info('Наличие продолжительности фильма' + res_min + ' подтверждено')
    else:
        self.page.loger_error('Наличие продолжительности фильма НЕ подтверждено')
    
    self.page.waitForElementVisible('.//div[@class="clip__age"]', 10)
    res_txt = str(self.result.find_link("div", "clip__age").text)  # Проверка наличия возрастного ограничения 12+
    assert ('+') in res_txt  # + - проверочное словосочетание надписи
    self.page.loger('Шаг 17. Наличие возрастного ограничения: ' + res_txt.strip() + ' подтверждено')
    time.sleep(1)

    self.page.loger('Проверка ссылок на странице:')
    
    res_txt = str(self.result.find_link("div", "clip__share")) # Проверка наличия ссылки "Поделиться
    assert ('Поделиться') in res_txt  # проверочное словосочетание надписи
    self.page.loger('Шаг 18. Наличие ссылки "Поделиться" подтверждено')
    time.sleep(1)
    
    res_txt = str(self.result.find_link("div", "clip__favorite"))   # Проверка наличия ссылки "В избранное""
    assert ('В избранное') in res_txt  
    self.page.loger('Шаг 19. Наличие ссылки "В избранное" подтверждено')
    time.sleep(1)
    
    res_txt = str(self.result.find_link("div", "clip__feedback"))  # Проверка наличия ссылки "Возникла проблема?"
    assert ('Возникла проблема?') in res_txt 
    self.page.loger('Шаг 20. Наличие ссылки "Возникла проблема?" подтверждено')
    time.sleep(1)

    self.driver.quit()