from .page import *

time.sleep(3)
def case_5_4(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 5_4  tvweb_new-5_4: Проверка карты тройка: удаление, привязка, наличие скидки \n')

    film = 'Путь домой'

    emailt = 'ttvzavr126@mail.ru'
    passw = '111111'
    
    time.sleep(2)
    self.page.click_f('Клик_Вход', 1)
    time.sleep(1)

    #self.page.send_f('Ввод_логина_вход', emailt, 2)
    self.driver.find_element_by_xpath('.//input[@class="authorization__login textbox"]').send_keys(emailt)
    time.sleep(1)

    #self.page.send_f('Ввод_пароля_вход', passw, 3)
    self.driver.find_element_by_xpath('.//input[@class="authorization__password textbox"]').send_keys(passw)
    time.sleep(2)

    self.page.click_f('Клик_Войти_auth', 2)
    time.sleep(8)

    self.prof.click_f('Клик_значок_пользователя', 3)
    time.sleep(4)

    self.page.loger('Шаг 4. Переход в личный кабинет')
    time.sleep(2)
    self.driver.find_element_by_xpath('.//a[@href="/profile/#tab=cabinet-account"]').click()  # Клик счет
    time.sleep(4)
    self.page.waitForElementVisible('.//h2[@class="cabinet-balance__heading"][contains(., "Баланс")]', 10)
    self.page.loger('Переход в личный кабинет подтвержден')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="bonuses-card__button button button_light button_stretched"]').click() # клик на информация тройка
    self.page.loger('Шаг 5. Произведен клик на "Информация" карты тройка')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content bonuses-form js-modal-content js-bonus-settings modal__content_open"]', 10) # Ожидание появления окна тройки
    self.page.loger('Появление окна информации Тройка подтверждено')
    time.sleep(1)

    res_txt = str(self.result.find_link("div", "modal__content bonuses-form js-modal-content js-bonus-settings modal__content_open"))  # Проверяет содержание окна
    assert('Карта Тройка') in res_txt
    assert('Информация о карте') in res_txt
    assert('Бонусы') in res_txt
    assert('Номер карты Тройка') in res_txt
    assert('toggle__label') in res_txt
    self.page.loger('Наличие информации о тройке подтверждено')
    time.sleep(2)

    self.page.loger('Шаг 6. Удаление карты:')
    self.driver.find_element_by_xpath('.//button[@class="bonuses-form__submit button button_light button_stretched"]').click() # Клик удалить карту
    self.page.loger('Карта тройка удалена')
    time.sleep(7)

    self.page.loger('Шаг 7. Привязка карты тройка:')
    self.page.waitForElementVisible('.//button[@class="bonuses-card__button button button_light button_stretched"]', 15)
    self.driver.find_element_by_xpath('.//button[@class="bonuses-card__button button button_light button_stretched"]').click() # Клик привязать карту
    self.page.loger('Клик привязать карту')
    time.sleep(2)

    self.page.waitForElementVisible('.//form[@class="modal__content bonuses-form js-modal-content js-bonus-binding modal__content_open"]', 10) # Проверка окна привязки тройки
    res_txt = str(self.result.find_link("form", "modal__content bonuses-form js-modal-content js-bonus-binding modal__content_open"))
    assert('Карта Тройка') in res_txt
    assert('Привязка карты') in res_txt
    assert('Номер карты Тройка') in res_txt
    self.page.loger('Содержание окна привязки карты тройка подтверждено')
    time.sleep(2)

    self.page.send_f('Ввод_номера_карты_тройка', '3996114243', 8) # Ввод номера тройки
    self.page.loger('Произведен ввод номера карты')
    time.sleep(1)
    self.driver.find_element_by_xpath('.//button[@class="bonuses-form__submit button button_stretched"][contains(., "Привязать")]').click() # Клик привязать карту
    self.page.loger('Карта тройка привязана')
    time.sleep(7)
    
    self.page.loger('Шаг 9. Сохранение количества бонусов')
    self.page.waitForElementVisible('.//button[@class="bonuses-card__button button button_light button_stretched"]', 15)
    self.driver.find_element_by_xpath('.//button[@class="bonuses-card__button button button_light button_stretched"]').click() # клик на "Информация" тройка
    time.sleep(3)
    
    rec_sic = (self.result.find_link("div", "bonuses-form__bonuses currency currency-RUB")) # копируем количество бонусов
    rec_text = rec_sic.text
    self.page.loger_info('Количество бонусов: ' + rec_sic.text)
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # Клик крестик
    time.sleep(2)

    self.page.loger('Шаг 10. Переход в фильм, чтобы проверить наличие скидки')
    time.sleep(2)

    self.page.send_f('Ввод_2_в_строку_поиска', film, 10)
    time.sleep(3)
    
    self.prof.click_f('Клик_поиска_Лупа', 11)
    time.sleep(4)
    
    self.driver.find_element_by_xpath('.//a[@href="/film/put-domoj/"]').click() # Клик на фильм Путь домой
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="clip__name heading-1"][contains(., "Путь домой")]', 10)
    time.sleep(3)
    self.page.loger('Переход в карточку фильма "Путь домой" подтвержден')

    self.driver.find_element_by_xpath('.//button[@id="clip-player-pay"]').click()
    self.page.loger('Шаг 12. Клик кнопки просмотр от 99 руб')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@data-clip="42903"]').click()
    self.page.loger('Клик кнопки напрокат SD 99р')
    time.sleep(3)

    self.page.waitForElementVisible('.//span[@class="payment-form__bonuses"]', 10)  # Проверяет наличие бонусов
    self.page.loger('Наличие скидки от карты тройка подтверждено')

    self.driver.quit()