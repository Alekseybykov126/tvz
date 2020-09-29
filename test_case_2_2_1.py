from .page import *

time.sleep(2)
def case_2_2_1(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_2_1 tvweb_new-2_2_1: Проверка фильтров поиска на странице Бесплатно(Жанры)')

    self.page.click_f('Клик_Бесплатно', 1)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click() # Кнопка развернуть
    time.sleep(1)
    self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 10)
    self.page.loger('Кнопка "Развернуть" работает')

    self.page.click_f('Клик_Жанры', 2)
    time.sleep(1)

    b = random.randint(0, 44)

    self.driver.find_elements_by_xpath('.//li[@data-filter-type="genres"]')[b].click()
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 4)
    time.sleep(1)

    genre1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_genres"]')
    genre1text = genre1.text
    self.page.loger('Выбранный жанр: ' + genre1text)
    time.sleep(2)

    m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильмов
    print(len(m))

    while (len(m)) == 0:
        self.driver.find_element_by_xpath('.//button[@class="filter__reset js-filter-reset"]').click() # Клик сбросить
        time.sleep(3)
        self.page.click_f('Клик_Бесплатно', 6)
        time.sleep(3)
        
        self.page.click_f('Клик_Жанры', 8)
        time.sleep(1)
        c = random.randint(0, 44)

        self.driver.find_elements_by_xpath('.//li[@data-filter-type="genres"]')[c].click()
        time.sleep(2)
        self.page.click_f('Клик_применить_фильтр', 4)

        genre1 = self.driver.find_element_by_xpath('.//button[@class="filter__item filter__item_genres"]')
        genre1text = genre1.text
        self.page.loger('Выбранный жанр: ' + genre1text)
        time.sleep(2)
        
        m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильвом
        print(len(m))

    p = random.randint(0, (len(m) - 1))
    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[p].click()
    time.sleep(3)  

    res_txt = str(self.result.find_link("h1", "clip__name heading-1").text)  # название фильма
    self.page.loger('Название фильма: ' + res_txt.strip())
    time.sleep(1)  
        
    genre2 = self.driver.find_element_by_xpath('.//div[@class="clip__genres"]')
    genre2text = genre2.text
    self.page.loger('Жанры в карточке фильма: ' + genre2text)
    time.sleep(2)

    assert (genre1text) in genre2text  # проверочное словосочетание надписи
    self.page.loger('Наличие жанра ' + genre1text + ' в карточке фильма подтверждено')
    time.sleep(1)

    self.driver.quit()