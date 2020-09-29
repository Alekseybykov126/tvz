from .page import * 
import random

def case_3_7(self, full_screen):

    emailt = 'ttvzavr126@mail.ru'
    passw = '111111'

    self.driver.get("https://www.tvzavr.ru/")
    self.page.loger_info('\n Тест кейс № 3_7 Проверка перехода в карточки фильмов в тематических подборках \n')   

    self.page.click_f('Клик_Подборки', 1)
    time.sleep(3)

    self.page.waitForElementVisible('.//h1[@class="page__heading superheading-1"]', 10) # Проверка перехода в раздел подборки
    res = str(self.result.find_link("h1", "page__heading superheading-1"))
    assert('тематические подборки фильмов') in res
    self.page.loger('Переход в раздел "Подборки" подтверждён')
    time.sleep(5)

    b = random.randint(1, 180)

    self.page.loger('Шаг 2. Переход в рандомную подборку')
    self.driver.find_elements_by_xpath('.//a[@class="card card_topic"]')[b].click()  # Клик по рандомной подборке
    time.sleep(3)

    name_topic = self.driver.find_element_by_xpath('.//h1[@class="page__heading superheading-1"]') # Проверка и печать названия подборки
    name_topic = name_topic.text
    self.page.loger('Осуществлен переход в подборку - ' + name_topic)
    time.sleep(1)


    m = self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')   # считает количество фильмов
    p = random.randint(0, (len(m) - 1))
    
    self.page.loger('Шаг 3. Переход в карточку фильма')
    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[p].click() # Клик на рандомный фильм
    time.sleep(2)

    name_film = self.driver.find_element_by_xpath('.//h1[@class="clip__name heading-1"]') # Просмотр заголовка
    name_film = name_film.text
    self.page.loger('Осуществлен переход в карточку фильма - ' + name_film)
    time.sleep(2)

    self.driver.back()
    time.sleep(3)

    g = random.randint(0, (len(m) - 1))

    self.page.loger('Шаг 4. Переход в карточку фильма')
    self.driver.find_elements_by_xpath('.//a[@class="card card_clip"]')[g].click() # Клик на рандомный фильм
    time.sleep(2)

    name_film = self.driver.find_element_by_xpath('.//h1[@class="clip__name heading-1"]') # Просмотр заголовка
    name_film = name_film.text
    self.page.loger('Осуществлен переход в карточку фильма - ' + name_film)
    time.sleep(2)

    
    
    
    self.driver.quit()

    
    

                    
                             