from .page import *

time.sleep(2)
def case_2_1_8(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 2_1_8 tvweb_new-2_1_8: Проверка фильтров поиска на странице Каталог(Бесплатно)')

    time.sleep(1)
    self.page.click_f('Клик_Каталог', 35)
    time.sleep(4)
    self.driver.find_element_by_xpath('.//span[@class="toggle__label"][contains(., "Бесплатные")]').click()  # клик Бесплатные
    self.page.loger('Поставил галочку на Бесплатные')
    time.sleep(3)
    self.page.click_f('Клик_постер_первого_фильма', 36)
    time.sleep(6)
    
    self.page.loger_info('Проверка воспроизведения и видимости надписи "Отключите рекламу за 1 рубль":') # Проверка видимости элемента
    self.page.waitForElementVisible('.//span[@class="tvz-button_disable_ad tvz-button_disable_ad js-trial-info"]', 10)
    rec_tit = str(self.result.find_link("span", "tvz-button_disable_ad tvz-button_disable_ad js-trial-info"))
    assert('Отключите рекламу за 1 рубль') in rec_tit
    if 'hidden' not in rec_tit :
        self.page.loger_info('Фильм бесплатный, реклама воспроизводится, наличие надписи "Отключите рекламу за 1 рубль" подтверждено')
    else:
        self.page.loger_error('Рекламы нет , Отсутствует надпись "Отключите рекламу за 1 рубль"')
    time.sleep(5)
    
    self.driver.quit()    