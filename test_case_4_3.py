from Regress_web.page import * 

time.sleep(1)
def case_4_3(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 4_3 tvweb_new-4_3: Проверка работоспособности кнопок "Смотреть все" с главной страницы \n')

    time.sleep(2)
    ## Бесплатные фильмы
    self.page.loger('Шаг 1. Проверка наличия Покупки и Подписки в списке бесплатных фильмов')

    #self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-12"]')
    target.location_once_scrolled_into_view

    self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10) # Контейнер с фильмами
    status_txt = str(self.result.find_link("div", "compilation-216")) # Исключает Покупку и Подписку из списка фильмов
    assert('Покупка') not in status_txt
    assert('Подписка') not in status_txt
    self.driver.find_elements_by_xpath('.//button[@data-related-compilation-id="216"]')[1].click() # Клик стрелки прокрутки вправо
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10)
    status_txt = str(self.result.find_link("div", "compilation-216"))
    assert('Покупка') not in status_txt
    assert('Подписка') not in status_txt
    self.driver.find_element_by_xpath('.//button[@data-related-compilation-id="216"]').click() # Клик стрелки прокрутки влево
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@data-related-compilation-id="216"]').click() # Клик стрелки прокрутки влево
    self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10)
    status_txt = str(self.result.find_link("div", "compilation-216"))
    assert('Покупка') not in status_txt
    assert('Подписка') not in status_txt
    self.driver.find_element_by_xpath('.//button[@data-related-compilation-id="216"]').click() # Клик стрелки прокрутки влево
    self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10)
    status_txt = str(self.result.find_link("div", "compilation-216"))
    assert('Покупка') not in status_txt
    assert('Подписка') not in status_txt
    self.page.loger('В разделе "Бесплатные фильмы" отсутствуют платные и фильмы по подписке')
    time.sleep(2)

    self.page.loger('Шаг 2. Проверка перехода в раздел "Бесплатные фильмы" через кнопку "Смотреть все"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/besplatnye-filmy/"]').click()  # Клик на "Смотреть все"
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Бесплатные фильмы') in head_txt
    self.page.loger('Переход в раздел "Бесплатные фильмы" подтвержден')
    self.driver.back()
    time.sleep(3)

    ### Новинки
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-60"]')
    target.location_once_scrolled_into_view
    self.page.loger('Шаг 3. Проверка раздела "Новинки"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/novinki/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Новинки') in head_txt
    self.page.loger('Переход в раздел "Новинки" подтвержден')
    self.driver.back()
    time.sleep(3)

    ## Фильмы на Хэллоуин____________!
    self.page.loger('Шаг 4. Проверка раздела "Фильмы на Хэллоуин"')
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-suggestions-base"]')
    target.location_once_scrolled_into_view
    self.driver.find_element_by_xpath('.//a[@href="/catalog/helloween/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Фильмы на Хэллоуин') in head_txt
    self.page.loger('Переход в раздел "Фильмы на Хэллоуин" подтвержден')
    self.driver.back()
    time.sleep(3)

    ## Смотреть по подписке
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-216"]')
    target.location_once_scrolled_into_view
    self.page.waitForElementVisible('.//div[@id="compilation-60"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-60"]') # скролл до подборки на Хэллоуин
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@id="compilation-260"]', 10) # Контейнер с фильмами
    status_txt = str(self.result.find_link("div", "compilation-260")) # Исключает Покупку и Бесплатно из списка фильмов
    assert('Покупка') not in status_txt
    assert('Бесплатно') not in status_txt
    self.driver.find_elements_by_xpath('.//button[@data-related-compilation-id="260"]')[1].click() # Клик стрелки прокрутки вправо
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@id="compilation-260"]', 10)
    status_txt = str(self.result.find_link("div", "compilation-260"))
    assert('Покупка') not in status_txt
    assert('Бесплатно') not in status_txt
    self.driver.find_element_by_xpath('.//button[@data-related-compilation-id="260"]').click() # Клик стрелки прокрутки влево
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@data-related-compilation-id="260"]').click() # Клик стрелки прокрутки влево
    self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10)
    status_txt = str(self.result.find_link("div", "compilation-216"))
    assert('Покупка') not in status_txt
    assert('Бесплатно') not in status_txt
    self.driver.find_element_by_xpath('.//button[@data-related-compilation-id="260"]').click() # Клик стрелки прокрутки влево
    self.page.waitForElementVisible('.//div[@id="compilation-216"]', 10)
    status_txt = str(self.result.find_link("div", "compilation-216"))
    assert('Покупка') not in status_txt
    assert('Бесплатно') not in status_txt
    self.page.loger('В разделе "Смотреть по подписке" отсутствуют платные и бесплатные фильмы')
    time.sleep(2)

    self.page.loger('Шаг 5. Проверка перехода в раздел "Смотреть по подписке" через кнопку "Смотреть все"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/smotret-po-podpiske/"]').click()  # Клик на "Смотреть все"
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Смотреть по подписке') in head_txt
    self.page.loger('Переход в раздел "Смотреть по подписке" подтвержден')
    self.driver.back()
    time.sleep(3)
    

    ## Лучшие фильмы киностудии Paramount
    self.page.waitForElementVisible('.//div[@id="compilation-260"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-260"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 6. Проверка раздела "Лучшие фильмы киностудии Paramount"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/luchshie-filmy-kinostudii-paramount/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Лучшие фильмы киностудии Paramount') in head_txt
    self.page.loger('Переход в раздел "Лучшие фильмы киностудии Paramount" подтвержден')
    self.driver.back()
    time.sleep(3)

    ## Фильмы ужасов
    self.page.waitForElementVisible('.//div[@id="compilation-228"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-228"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 7. Проверка раздела "Фильмы ужасов"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/filmy-uzhasov/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Фильмы ужасов') in head_txt
    self.page.loger('Переход в раздел "Фильмы ужасов" подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на развернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10) 
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на свернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 10)
    time.sleep(1)
    self.page.loger('Кнопка Свернуть/Развернуть работает')
    self.driver.back()
    time.sleep(3)
    
    ### MoviesChain by tvzavr
    self.page.waitForElementVisible('.//div[@id="compilation-23"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-23"]') # скролл до подборки 
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 8. Проверка раздела "MoviesChain by tvzavr"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/movieschain/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('MoviesChain by tvzavr') in head_txt
    self.page.loger('Переход в раздел "MoviesChain by tvzavr" подтвержден')
    self.driver.back()
    time.sleep(3)

    ### Современные мультфильмы
    self.page.waitForElementVisible('.//div[@id="compilation-230"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-230"]') # скролл до подборки 
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 9. Проверка раздела "Современные мультфильмы"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/modern-cartoons/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Современные мультфильмы') in head_txt
    self.page.loger('Переход в раздел "Современные мультфильмы" подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на развернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10) 
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на свернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 10)
    time.sleep(1)
    self.page.loger('Кнопка Свернуть/Развернуть работает')
    self.driver.back()
    time.sleep(3)

    ## Лучшие ремейки
    self.page.waitForElementVisible('.//div[@id="compilation-6"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-6"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 10. Проверка раздела "Лучшие ремейки"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/luchshie-remeyki/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Лучшие ремейки') in head_txt
    self.page.loger('Переход в раздел "Лучшие ремейки" подтвержден')
    self.driver.back()
    time.sleep(3)

    ## Молодёжные комедии
    self.page.waitForElementVisible('.//div[@id="compilation-279"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-279"]') # скролл до подборки 
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 11. Проверка раздела "Молодёжные комедии"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/molodezhnye-komedii/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Молодёжные комедии') in head_txt
    self.page.loger('Переход в раздел "Молодёжные комедии" подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на развернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10) 
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на свернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 10)
    time.sleep(1)
    self.page.loger('Кнопка Свернуть/Развернуть работает')
    self.driver.back()
    time.sleep(3)

    ## Французские фильмы
    self.page.waitForElementVisible('.//div[@id="compilation-139"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-139"]') # скролл до подборки 
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 12. Проверка раздела "Французские фильмы"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/frantsuzskie-filmy/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Французские фильмы') in head_txt
    self.page.loger('Переход в раздел "Французские фильмы" подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на развернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10) 
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на свернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 10)
    time.sleep(1)
    self.page.loger('Кнопка Свернуть/Развернуть работает')
    self.driver.back()
    time.sleep(3)

    ## Психологические триллеры
    self.page.waitForElementVisible('.//div[@id="compilation-18"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-18"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 13. Проверка раздела "Психологические триллеры"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/psihologicheskie-trillery/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Психологические триллеры') in head_txt
    self.page.loger('Переход в раздел "Психологические триллеры" подтвержден')
    self.driver.back()
    time.sleep(3)

    ### Советские мультфильмы
    self.page.waitForElementVisible('.//div[@id="compilation-91"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-91"]') # скролл до подборки 
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 14. Проверка раздела "Советские мультфильмы"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/sovetskie-multfilmy/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Советские мультфильмы') in head_txt
    self.page.loger('Переход в раздел "Советские мультфильмы" подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на развернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10) 
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на свернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 10)
    time.sleep(1)
    self.page.loger('Кнопка Свернуть/Развернуть работает')
    self.driver.back()
    time.sleep(3)

    ### Высокобюджетные фильмы
    self.page.waitForElementVisible('.//div[@id="compilation-17"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-17"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 15. Проверка раздела "Высокобюджетные фильмы"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/vysokobyudzhetnye-filmy/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Высокобюджетные фильмы') in head_txt
    self.page.loger('Переход в раздел "Высокобюджетные фильмы" подтвержден')
    self.driver.back()
    time.sleep(3)

    ### Фильмы из Топ-250 КиноПоиска
    self.page.waitForElementVisible('.//div[@id="compilation-41"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-41"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 16. Проверка раздела "Фильмы из Топ-250 КиноПоиска"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/filmy-iz-top-250-kinopoiska/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Фильмы из Топ-250 КиноПоиска') in head_txt
    self.page.loger('Переход в раздел "Фильмы из Топ-250 КиноПоиска" подтвержден')
    self.driver.back()
    time.sleep(3)

    ### Фильмы, основанные на реальных событиях
    self.page.waitForElementVisible('.//div[@id="compilation-48"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-48"]') # скролл до подборки Смотреть по подписке
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 17. Проверка раздела "Фильмы, основанные на реальных событиях"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/filmy-osnovannye-na-realnyh-sobytiyah/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Фильмы, основанные на реальных событиях') in head_txt
    self.page.loger('Переход в раздел "Фильмы, основанные на реальных событиях" подтвержден')
    self.driver.back()
    time.sleep(3)

    ### Биографические фильмы
    self.page.waitForElementVisible('.//div[@id="compilation-26"]', 10)  
    target = self.driver.find_element_by_xpath('.//div[@id="compilation-26"]') # скролл до подборки 
    target.location_once_scrolled_into_view # скролл
    time.sleep(2)

    self.page.loger('Шаг 18. Проверка раздела "Биографические фильмы"')
    self.driver.find_element_by_xpath('.//a[@href="/catalog/biograficheskie-filmy/"]').click()
    time.sleep(3)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    head_txt = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('Биографические фильмы') in head_txt
    self.page.loger('Переход в раздел "Биографические фильмы" подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на развернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10) 
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()  # Клик на свернуть
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 10)
    time.sleep(1)
    self.page.loger('Кнопка Свернуть/Развернуть работает')
    self.driver.back()
    time.sleep(3)

    self.driver.quit()