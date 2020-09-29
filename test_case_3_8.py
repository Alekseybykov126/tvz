from .page import * 

def case_3_8(self, full_screen):
    
   self.driver.get("https://www.tvzavr.ru/")                   
   self.page.loger('\n Запуск Тест кейс № 3_8 tvweb_new-3_8: Проверка статуса фильмов в разделах "Подписка tvzavr +" и "Отключи рекламу на tvzavr!" \n')  

   self.page.click_f('Клик_Новинки', 1)
   time.sleep(2)
   self.page.click_f('Клик_Подписки', 2)
   time.sleep(2)

   self.page.loger('Шаг 3. Проверка кнопки "Развернуть/Свернуть" в разделе "Подписка tvzavr +": ')
   self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()   # Развернуть текст
   time.sleep(1)
   self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 5) # проверка открытия текста
   self.page.loger('Кнопка "Развернуть" работает и разворачивает текст')
   time.sleep(1)
   self.driver.find_element_by_xpath('.//button[@class="rollup__toggle js-rollup-toggle"]').click()   # Свернуть текст
   time.sleep(1)
   self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 3)
   self.page.loger('Кнопка "Свернуть" работает и сворачивает текст.')

   self.page.loger('Шаг 4. Проверка статуса фильмов в разделе "Подписка tvzavr +":')
   self.page.waitForElementVisible('.//div[@class="catalog__cards js-catalog-cards"]', 10) # Контейнер с фильмами
   res_txt = str(self.result.find_link("div", "catalog__cards js-catalog-cards")) # Тут проверяю, что в контейнере нет фильмов со статусами "подписка" и "купить"
   assert('Бесплатно') not in res_txt
   assert('Покупка') not in res_txt
   self.page.loger('На странице "Подписка tvzavr +" фильмы только по подписке.')
   time.sleep(2)

   self.page.click_f('Клик_Подписка_Отключи_рекламу', 5)
   time.sleep(2)
   self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)  # Вверх страниицы
   self.driver.refresh()                                                             # Обновить страницу

   self.page.loger('Шаг 6. Проверка кнопки "Развернуть/Свернуть" в разделе "Отключи рекламу на tvzavr!": ')
   self.driver.find_element_by_xpath('//*[@id="disabled-ads"]/div[2]/div/button').click()   # Развернуть текст
   time.sleep(1)
   self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow rollup_open"]', 3)
   self.page.loger('Кнопка "Развернуть" работает и разворачивает текст')
   time.sleep(1)
   self.driver.find_element_by_xpath('//*[@id="disabled-ads"]/div[2]/div/button').click()   # Свернуть текст
   time.sleep(1)
   self.page.waitForElementVisible('.//div[@class="page__description seo-info rollup js-rollup rollup_overflow"]', 3)
   self.page.loger('Кнопка "Свернуть" работает и сворачивает текст')

   self.page.loger('Шаг 7. Проверка статуса фильмов в разделе "Отключи рекламу на tvzavr!":')
   self.page.waitForElementVisible('.//div[@class="catalog__cards js-catalog-cards"]', 10) # Контейнер с фильмами
   res_txt = str(self.result.find_link("div", "catalog__cards js-catalog-cards")) # Тут проверяю, что в контейнере нет фильмов со статусами "подписка" и "купить"
   assert('Подписка') not in res_txt
   assert('Покупка') not in res_txt
   self.page.loger('На странице "Отключи рекламу на tvzavr!" только бесплатные фильмы')
   time.sleep(2)   

   self.driver.quit()