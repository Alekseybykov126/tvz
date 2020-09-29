from .page import * 

def case_6_4(self, full_screen):

    self.driver.get("https://www.tvzavr.ru/")
    self.page.loger_info('\n Тест кейс № 6_4 tvweb_new-6_4: Проверка работы карты сайта \n')
    time.sleep(1)

    self.page.click_f('Переход_вниз_страницы', 1)
    time.sleep(3)
    self.page.click_f('Переход_вниз_страницы', 2)
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="sitemap__heading heading-1"]', 10)   # Проверка заголовка страницы карта сайта
    res_txt = str(self.result.find_all_link("h1", "sitemap__heading heading-1"))
    assert('Карта сайта') in res_txt
    self.page.loger('Шаг 3. Переход в раздел "Карта сайта" подтвержден')

    self.page.waitForElementVisible('.//div[@class="sitemap__links"]', 10)    # Проверка наличия ссылок на странице
    res_txt = str(self.result.find_all_link("div", "sitemap__links"))
    assert('Главная') in res_txt
    assert('Новинки') in res_txt
    assert('Подписки') in res_txt
    assert('Бесплатно') in res_txt
    assert('Каталог') in res_txt
    assert('Тематические подборки') in res_txt
    assert('Кидбург') in res_txt
    assert('Детям') in res_txt
    assert('Приложение tvzavr на устройствах') in res_txt
    assert('Приложение tvzavr для Android') in res_txt
    assert('Приложение tvzavr для iOS') in res_txt
    self.page.loger('Шаг 4. Наличие всех ссылок на странице "Карта сайта" подтверждено')

    # # Главная
    self.driver.find_element_by_xpath('.//a[@class="sitemap__link"]').click()    # Клик на первую ссылку "Главная"
    time.sleep(3)

    self.page.waitForElementVisible('.//div[@class="owl-item active"]', 10)
    self.page.loger('Переход по ссылке на "Главную" страницу подтвержден')
    time.sleep(1)

    self.page.click_f('Переход_вниз_страницы', 5)
    time.sleep(2)
    self.page.click_f('Переход_вниз_страницы', 5)
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)

    # # Новинки
    self.driver.find_element_by_xpath('.//a[@href="/novinki/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert('Новинки кино') in res_txt
    self.page.loger('Шаг 6. Переход в раздел "Новинки" подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 7)
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)
    
    
    # # Подписки
    self.driver.find_element_by_xpath('.//a[@href="/subscription/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="subscriptions__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "subscriptions__heading superheading-1"))
    assert('Подписка «tvzavr+»') in res_txt
    self.page.loger('Шаг 8. Переход в раздел "Подписки" подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 9)
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)

    # # Бесплатно
    self.driver.find_element_by_xpath('.//a[@href="/besplatno/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert('Бесплатные фильмы') in res_txt
    self.page.loger('Шаг 10. Переход в раздел Бесплатные фильмы подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 11)
    time.sleep(2)
    

    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)


    # # Каталог
    self.driver.find_element_by_xpath('.//a[@href="/genres/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert('Кино по жанрам') in res_txt
    self.page.loger('Шаг 12. Переход в раздел Кино по жанрам подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 13)
    time.sleep(2)
    

    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)


    # # Тематические подборки
    self.driver.find_element_by_xpath('.//a[@href="/topics/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert('тематические подборки фильмов') in res_txt
    self.page.loger('Шаг 14. Переход в раздел Тематические подборки подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 15)
    time.sleep(3)
    
    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(5)


    # # Кидбург
    self.driver.find_element_by_xpath('.//a[@href="/kidburg/"]').click()
    time.sleep(4)

    self.page.waitForElementVisible('.//p[@class="kidburg-title"]', 10)
    res_txt = str(self.result.find_all_link("p", "kidburg-title"))
    assert('Киностудия') in res_txt
    self.page.loger('Шаг 16. Переход в раздел Кидбург подтвержден')
    time.sleep(2)

    self.driver.back()

    ## Детям
    self.driver.find_element_by_xpath('.//a[@href="/kids/"]').click() 
    time.sleep(2)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "page__heading superheading-1"))
    assert('Детские мультфильмы') in res_txt
    self.page.loger('Шаг 16. Переход в раздел Детям подтвержден')
    time.sleep(2)

    self.driver.back()

    # Приложение tvzavr на устройствах
    self.driver.find_element_by_xpath('.//a[@href="/apps/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="apps__heading superheading-1"]', 10)
    res_txt = str(self.result.find_all_link("h1", "apps__heading superheading-1"))
    assert('Смотри tvzavr') in res_txt
    self.page.loger('Переход в раздел Приложение tvzavr на устройствах подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 17)
    time.sleep(2)
    

    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)


    # # Приложение tvzavr для Android
    self.driver.find_element_by_xpath('.//a[@href="/apps/android/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="app-mobile__heading"]', 10)
    res_txt = str(self.result.find_all_link("h1", "app-mobile__heading"))
    assert(' для Android') in res_txt
    self.page.loger('Шаг 18. Переход в раздел Приложение tvzavr для Android подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 19)
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)

    # # Приложение tvzavr для IOS
    self.driver.find_element_by_xpath('.//a[@href="/apps/ios/"]').click()
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="app-mobile__heading"]', 10)
    res_txt = str(self.result.find_all_link("h1", "app-mobile__heading"))
    assert(' для iOS') in res_txt
    self.page.loger('Шаг 20. Переход в раздел Приложение tvzavr для IOS подтвержден')
    time.sleep(2)

    self.page.click_f('Переход_вниз_страницы', 21)
    time.sleep(2)
    

    self.driver.find_element_by_xpath('.//a[@href="/sitemap/"][contains(., "Карта сайта")]').click()  # Клик Карта сайта внизу страницы
    time.sleep(2)

    self.page.loger('Проверка всех ссылок карты сайта завершена успешно')

    self.driver.quit()