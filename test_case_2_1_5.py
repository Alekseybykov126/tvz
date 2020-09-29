from .page import *

time.sleep(2)
def case_2_1_5(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_1_5 tvweb_new-2_1_5: Проверка фильтров поиска на странице Каталог(Аудио)')

    time.sleep(1)
    self.page.click_f('Клик_Каталог', 29)
    time.sleep(2)

    rec_sic = (self.result.find_link("div", "card__title")) # копируем название первого фильма в списке бесплатных фильмов
    rec_text = rec_sic.text
    self.page.loger_info('Название фильма до применения фильтра аудио Китайский: ' + rec_sic.text)
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="filter__subcategory js-filter-subcategory"][contains(., "Языки")]').click() # Клик язык аудио
    time.sleep(1)
    self.driver.find_element_by_xpath('.//li[@data-filter-id="52496"]').click() # Клик Китайский
    time.sleep(1)
    self.page.click_f('Клик_применить_фильтр', 30)
    time.sleep(2)

    rec_sic2 = (self.result.find_link("div", "card__title")) # копируем название первого фильма 
    rec_text2 = rec_sic2.text
    self.page.loger_info('Название первого фильма с фильтром аудио Китайский: ' + rec_sic2.text)
    time.sleep(2)

    if rec_sic.text != rec_sic2.text:
        self.page.loger('Фильтр Язык аудио применился')
    else:
        assert(), "Фильтр Язык аудио не применился"
    time.sleep(2)   

    self.driver.quit()