from page import *

time.sleep(3)
def case_6_1(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 6_1 tvweb_new-6_1: Проверка работоспособности верхних разделов \n')

    # Автоматическая смена слайдов
    self.page.loger('Шаг 1. Проверка автоматической смены слайдов')
    slide_1 = str(self.result.find_x("div", "owl-item active")) 
    self.page.loger('Слайд до автоматической смены: ' + slide_1)
    time.sleep(12)  # Время, необходимое для авто смены слайда
    slide_2 = str(self.result.find_x("div", "owl-item active"))
    self.page.loger('Слайд после автоматической смены: ' + slide_2)
    time.sleep(1)
    if slide_1 != slide_2:
        self.page.loger('Шаг 2. Автоматическая смена слайдов подтверждена')
    else:
        self.page.loger('Не подтверждена автоматическая смена слайдов')
    time.sleep(2)

    # Прокрутка слайда вправо
    self.page.loger('Шаг 3. Проверка прокрутки слайда вправо')
    time.sleep(9) # время, чтобы слайд сменился перед прокруткой
    self.page.waitForElementVisible('.//div[@class="owl-item active"]', 10)  # Смотрит на активный слайд
    slide_1 = str(self.result.find_x("div", "owl-item active"))
    self.page.loger('Слайд до прокрутки вправо: ' + slide_1)    # вывод на экран первого фильма
    self.driver.find_element_by_xpath('.//button[@class="slider__navigation slider__navigation_next js-slider-navigation js-slider-navigation-next"]').click() # Клик прокрутка вправо
    self.page.loger('Шаг 4. Клик кнопки прокрутки слайда вправо произведен')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="owl-item active"]', 10) # проверка слайда после прокрутки вправо
    slide_2 = str(self.result.find_x("div", "owl-item active"))    
    self.page.loger('Слайд после прокрутки вправо: ' + slide_2)   # вывод на экран второго фильма
    if slide_1 != slide_2:
        self.page.loger('Шаг 5. Смена слайдов при прокрутке слайда вправо подтверждена')
    else:
        self.page.loger_error('Не подтверждена cмена слайдов при прокрутке вправо')
    time.sleep(2)

    # Прокрутка слайда влево
    self.page.loger('Шаг 6. Проверка прокрутки слайда влево')
    time.sleep(9)
    self.page.waitForElementVisible('.//div[@class="owl-item active"]', 10)
    slide_1 = str(self.result.find_x("div", "owl-item active"))
    self.page.loger('Слайд до прокрутки влево: ' + slide_1)
    self.driver.find_element_by_xpath('.//button[@class="slider__navigation slider__navigation_prev js-slider-navigation js-slider-navigation-prev"]').click() # Клик прокрутка влево
    self.page.loger('Шаг 7. Клик кнопки прокрутки слайда влево произведен')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="owl-item active"]', 10)  # проверка слайда после прокрутки влево
    slide_2 = str(self.result.find_x("div", "owl-item active"))
    self.page.loger('Слайд после прокрутки слайда влево: ' + slide_2)
    if slide_1 != slide_2:
        self.page.loger_info('Шаг 8. Смена слайдов при прокрутке слайда влево подтверждена')
    else:
        self.page.loger_info('Не подтверждена cмена слайдов при прокрутке влево')
    time.sleep(2)
    
    self.page.click_f('Клик_поиска_Лупа', 9)
    time.sleep(1)
    
    self.page.waitForElementVisible('.//div[@class="search__message tvz-alerts"]', 10) # Проверка сообщения под строкой поиска
    res_txt = str(self.result.find_all_link("div", "search__message tvz-alerts"))  # Проверка наличия надписи  
    assert ('В запросе недостаточно символов. Пожалуйста, продолжите ввод.') in res_txt  # проверочное словосочетание надписи
    self.page.loger('Шаг 10. Наличие сообщения "В запросе недостаточно символов. Пожалуйста, продолжите ввод." подтверждено')
    time.sleep(2)
    
    self.page.send_f('Ввод_в_строку_поиска', 'Большой', 11) 
    time.sleep(1)
    self.page.loger('Шаг 12. Ввод в строку поиска слова "человек" произведен')
    
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"]', 10)   # Проверка изменения содержания страницы после ввода слова самый 
    res_txt = str(self.result.find_link("div", "search-clip__title subheading-1"))  #search_form_results_clip_name
    assert ('Большой') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 13. Изменение содержания страницы после ввода слова поиска "самый" подтверждено')
    time.sleep(1)

    self.page.send_f('Ввод_в_строку_поиска', ' куш', 14)   # Ввод в строку поиска слова "опасный"
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"]', 10)
    res_txt = str(self.result.find_link("div", "search-clip__title subheading-1"))     # Проверка изменения содержания страницы после ввода слова поиска "самый опасный"
    assert ('Большой куш') in res_txt # Самый опасный человек - проверочное словосочетание надписи
    self.page.loger('Шаг 15. Изменение содержания страницы после ввода слова поиска "Большой куш" подтверждено')
    time.sleep(2)

    self.page.click_f('Клик_кнопки_крестик', 16)
    time.sleep(2)
    
    self.page.click_f('Клик_Новинки', 17)
    time.sleep(3)
   
    self.page.click_f('Переход_вниз_страницы', 18)
    time.sleep(2)
    self.page.click_f('Показать_еще', 19)
    time.sleep(2)
    self.page.click_f('Клик_Подписки', 20)
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="subscriptions__heading superheading-1"]', 10)  # Проверка Переход на страницу "Подписка tvzavr+"
    res_txt = str(self.result.find_all_link("h1", "subscriptions__heading superheading-1")) 
    assert ('Подписка «tvzavr+»') in res_txt    # Подписка tvzavr+ - проверочное словосочетание надписи
    self.page.loger('Шаг 21. Переход на страницу "Подписка tvzavr+" подтверждено')
    time.sleep(2)
    
    self.page.click_f('Клик_Подписка_Отключи_рекламу', 22)
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="subscriptions__heading superheading-1"]', 10)  # Проверка Переход на страницу «Отключи рекламу на tvzavr!»
    res_txt = str(self.result.find_all_link("h1", "subscriptions__heading superheading-1"))  
    assert ('«Отключи рекламу на tvzavr!»') in res_txt    # «Отключи рекламу на tvzavr!» - проверочное словосочетание надписи
    self.page.loger('Шаг 23. Переход на страницу "Отключи рекламу на tvzavr!" подтверждено')
    time.sleep(2)
      
    self.page.click_f('Клик_Бесплатно', 24)
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)   # Проверка Переход на страницу "Бесплатно"
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert ('Бесплатные фильмы') in res_txt   # проверочное словосочетание надписи
    self.page.loger('Шаг 25. Переход на страницу "Бесплатно" подтверждено')
    time.sleep(2)

    self.page.click_f('Клик_Подборки', 26)
    time.sleep(2)
    
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка Переход на страницу "Подборки"
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert ('тематические подборки фильмов') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 27. Переход на страницу "Подборки" подтвержден')
    time.sleep(2)

    # self.page.click_f('Клик_Коллекции', 28)
    # time.sleep(3)
    # self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка Переход на страницу "Коллекции"
    # res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    # assert ('Коллекции') in res_txt  # проверочное словосочетание надписи
    # self.page.loger('Шаг 29. Переход на страницу "Коллекции" подтвержден')
    # time.sleep(2)

    self.page.click_f('Клик_Подборки_партнеров', 30)
    time.sleep(2)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка Переход на страницу Подборки партнеров
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert ('Подборки партнеров') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 31. Переход на страницу "Подборки партнеров" подтвержден')
    time.sleep(2)

    self.page.click_f('Клик_Каталог', 32)
    time.sleep(2)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка Переход на страницу Каталог
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert ('Кино по жанрам') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 33. Переход на страницу "Кино по жанрам" подтвержден')
    time.sleep(2)
    
    self.page.click_f('Клик_Детям', 34)
    time.sleep(2)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка Переход на страницу Детям
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert ('Детские мультфильмы') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 35. Переход на страницу "Детские мультфильмы" подтвержден')
    time.sleep(2)
    
    self.page.click_f('Клик_Спецпроекты', 36)
    time.sleep(2)
    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка Переход на страницу Спецпроекты
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert ('спецпроекты') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 37. Переход на страницу "спецпроекты" подтвержден')
    time.sleep(2)
    
    self.page.click_f('Клик_Кино_равного_доступа', 38)
    time.sleep(2)
    self.page.waitForElementVisible('.//div[@class="promocode-header__title"]', 10) # Проверка Переход на страницу Кино равного доступа
    res_txt = str(self.result.find_all_link("div", "promocode-header__title"))
    assert ('Кино равного доступа') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 39. Переход на страницу "Кино равного доступа" подтвержден')
    self.driver.back()
    time.sleep(2)

    self.page.click_f('Проект, где ваши дети снимаются в кино', 40)
    time.sleep(2)
    self.page.waitForElementVisible('.//p[@class="kidburg-title"]', 10) # Проверка Переход на страницу Проект, где ваши дети снимаются в кино
    res_txt = str(self.result.find_all_link("p", "kidburg-title"))
    assert ('Киностудия') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 41. Переход на страницу "Проект, где ваши дети снимаются в кино" подтвержден')
    self.driver.back()
    time.sleep(2)

    self.page.click_f('Клик_Вход', 42) 
    time.sleep(1)
    res_txt = str(self.result.find_all_link("a", "tabs__link js-tabs-link"))  # Проверка появления окна авторизации
    assert ('Вход') in res_txt # проверочное словосочетание надписи
    self.page.loger('Шаг 43. Появление диалога авторизации подтверждено')
    time.sleep(1)

    # self.page.tester_click_xpath('//a[@class="auth_restore-password"]')
    # self.page.loger_info('Шаг 44. Кнопка "Напомнить пароль" кликабельна')
    # time.sleep(1)

    self.page.click_f('Клик_кнопки_крестик', 45)
    time.sleep(1)

    self.driver.quit()