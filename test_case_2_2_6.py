from .page import *

time.sleep(2)
def case_2_2_6(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_2_6 tvweb_new-2_2_6: Проверка фильтров поиска на странице Бесплатно(Субтитры)')
   
    time.sleep(1)
    self.page.click_f('Клик_Бесплатно', 31)
    time.sleep(2)

    rec_sic = (self.result.find_link("div", "card__title")) # копируем название первого фильма в списке бесплатных фильмов
    rec_text = rec_sic.text
    self.page.loger_info('Название первого фильма до выбора фильтра субтитров на Русском: ' + rec_sic.text)
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="filter__subcategory js-filter-subcategory"][contains(., "Языки")]').click() # Клик языки
    time.sleep(1)
    self.driver.find_element_by_xpath('.//a[@data-target="filter-subtitles"][contains(., "Субтитры")]').click() # Клик субтитры
    time.sleep(1)

    self.driver.find_element_by_css_selector('#filter-subtitles .filter__link:nth-child(2)').click() # Клик на русский язык
    time.sleep(2)
    self.page.click_f('Клик_применить_фильтр', 32)
    time.sleep(2)

    rec_sic2 = (self.result.find_link("div", "card__title")) # копируем название первого фильма в списке бесплатных фильмов
    rec_text2 = rec_sic2.text
    self.page.loger_info('Название первого фильма после выбора фильтра субтитров на русском: ' + rec_sic2.text)
    time.sleep(2)

    if rec_sic.text != rec_sic2.text:
        self.page.loger('Фильтр Язык субтитров применился')
    else:
        assert(), "Фильтр Язык субтитров не применился"
    time.sleep(2)

    self.driver.quit()