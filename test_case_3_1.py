from .page import *

def case_3_1(self, full_screen):
    self.page.loger_info('\n Запуск Тест кейс № 3_1  tvweb_new-3_1: Проигрывание бесплатных фильмов и взаимодействие с плеером \n')
    
                
    time.sleep(1)
    self.page.click_f('Клик_Бесплатно', 1)
    time.sleep(4)
    b = random.randint(1, 23)

    self.page.loger('Шаг 2. Получение названия случайного фильма')
    remember_name = self.driver.find_elements_by_xpath("//div[@class='card__title']")[b] # запоминание названия рандомного фильма
    remember_name = remember_name.get_attribute('innerHTML')
    self.page.loger('  Название фильма: ' + remember_name)
    time.sleep(2)   

    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[b].click()  # Клик на фильм
    time.sleep(5)

    target = self.driver.find_element_by_xpath('.//h1[@class="clip__name heading-1"]') # скролл до заголовка с названием фильма
    target.location_once_scrolled_into_view # скролл

    self.page.loger('Шаг 3. Проверка воспроизведения рекламы')
    self.page.waitForElementVisible('.//span[@class="tvz-button_disable_ad tvz-button_disable_ad js-trial-info"]', 10)   # Проверка видимости надписи "Отключите рекламу за 1 рубль"
    rec_tit = str(self.result.find_link("span", "tvz-button_disable_ad tvz-button_disable_ad js-trial-info"))   # Проверка видимости надписи "Отключите рекламу за 1 рубль"
    if 'hidden' not in rec_tit :
        self.page.loger_info('  Реклама воспроизводится, наличие надписи "Отключите рекламу за 1 рубль" подтверждено')
    else:
        self.page.loger_error('Рекламы нет! , Отсутствует надпись "Отключите рекламу за 1 рубль"')
    time.sleep(100) # долго, чтобы успела закончиться реклама

    
    self.page.loger('Шаг 4. Получение времени для сравнения воспроизведения:')
    pyautogui.moveTo(1300, 460, duration = 1)   # двигаем, чтобы показались кнопки плеера
    pyautogui.moveTo(1000, 600, duration = 1)
    time1 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]') # Значение времени 1, чтобы потом сравнить проигрывается ли фильм
    time1text = time1.text
    self.page.loger("  Первое значение времени: "  + time1text)    
    time.sleep(7)
    
    self.page.loger('Шаг 5. Сравнение названий фильма на странице "Бесплатно" и в плеере: ')
    pyautogui.moveTo(1303, 450, duration = 1)  # двигаем, чтобы показались кнопки плеера
    self.page.tester_vis_xpath('.//span[@class="tvz-ad_title"]')  # Проверка появления названия фильма в заголовке плеера
    resic = (self.result.find_link("div", "tvz-movie_title")).text
    self.page.loger_info("  Название фильма в заголовке плеера: " + resic)
    time.sleep(2)

    if remember_name != resic:    # проверка совпадения названия в плеере и на странице Бесплатно     
        assert(), "Названия фильма на странице 'Бесплатно' и в плеере не совпадают"
    else:
        self.page.loger('  Названия совпадают')
    time.sleep(4) 

    pyautogui.moveTo(1301, 462, duration = 1)   # двигаем, чтобы показались кнопки плеера
    pyautogui.moveTo(1001, 602, duration = 1)
    time2 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]')  # Значение времени 2, чтобы потом сравнить проигрывается ли фильм
    time2text = time2.text
    self.page.loger("  Второе значение времени для сравнения воспроизведения: " + time2text)

    if time1text < time2text:                # сравнение времени, чтобы определить проигрывание фильма
        self.page.loger('  Значение времени 1: ' + time1text + ' меньше времени 2: ' + time2text + ' значит, фильм воспроизводится')
    else:
        assert(), "Значения времени одинаковые, фильм " + remember_name + " не проигрывается"
    time.sleep(3)
    
    self.page.loger('Шаг 6. Проверка включения и отключения звука:')
    pyautogui.moveTo(1305, 468, duration = 1)   # двигаем, чтобы показались кнопки плеера
    pyautogui.moveTo(1010, 620, duration = 1)
    self.driver.find_element_by_xpath('.//div[@class="tvz-button_volume-icon"][@data-state="playing"]').click()  # два значения элемента потому, что просто data-state="playing" - это воспроизведение/пауза
    self.page.loger('  Убрал звук')
    time.sleep(3)

    pyautogui.moveTo(1300, 460, duration = 1)   # двигаем, чтобы показались кнопки плеера
    pyautogui.moveTo(1000, 600, duration = 1)
    self.driver.find_element_by_xpath('.//div[@data-state="volume-off"]').click() # а с таким значением только один элемент
    self.page.loger('  Включил звук')
    time.sleep(4)

    self.page.loger('Шаг 7. Проверка перемотки фильма:')
    pyautogui.moveTo(1301, 462, duration = 1)   # двигаем, чтобы показались кнопки плеера
    time3 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]') # Берём значение времени, чтобы проверить перемотку 
    time3text = time3.text
    self.page.loger("  Время до перемотки: " + time3text)
    time.sleep(3)

    pyautogui.moveTo(1300, 460, duration = 1)   # двигаем, чтобы показались кнопки плеера
    pyautogui.click(1110, 820, duration = 2)  # перемотка 
    time.sleep(4)

    pyautogui.moveTo(1303, 461, duration = 1)  # двигаем, чтобы показались кнопки плеера
    time4 = self.driver.find_element_by_xpath('.//span[@class="tvz-time_label tvz-timerow-current_time"]')  # Берём второе значение времени, чтобы проверить перемотку
    time4text = time4.text
    self.page.loger("  Время после перемотки: " + time4text)
    time.sleep(2)

    if time3text != time4text:     # сравнение значений времени, чтобы определить перемотку фильма
        self.page.loger('  Фильм ' + remember_name + ' перематывается')
    else:
        assert(), "Фильм " + remember_name + " не перематывается"
    time.sleep(2)

        
    pyautogui.moveTo(1319, 500, duration = 1)  # двигаем, чтобы показались кнопки плеера
    self.card.click_f('Клик_пауза', 8)
    time.sleep(1)

    ### Добавить проверку, что фильм стоит на паузе

    self.driver.quit()