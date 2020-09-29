from .page import * 

def case_6_2(self, full_screen):

   self.driver.get("https://www.tvzavr.ru/")                   
   self.page.loger('\n Запуск Тест кейс № 6_2 tvweb_new-6_2: Проверка перехода по нижним ссылкам и отправка письма в службу поддержки (кроме "Приложения" и "Карта сайта") \n')  

   email = 'tvzavrtest.test@mail.ru'
   passw = 'Test315492'
   name_user = 'tvzavrtest.test@mail.ru'

   self.page.click_f('Переход_вниз_страницы', 1)
   time.sleep(3)
   self.page.click_f('Переход_вниз_страницы', 2)
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="footer__container"]', 27) # Проверка наличия всех элементов нижнего контейнера
   res_txt = str(self.result.find_all_link("div", "footer__container"))
   
   self.driver.find_element_by_xpath('.//a[@class="page__topper topper page__topper_displayed"]').click()
   self.page.loger('Шаг 4. Наличие кнопки "Вверх" подтверждено, нажал')

   self.page.click_f('Переход_вниз_страницы', 5)
   time.sleep(3)
   self.page.click_f('Переход_вниз_страницы', 6)

   
   self.page.waitForElementVisible('//span[@class="footer__label"][contains(., "Контакт для прессы: ")]', 7) # найти Контакт для прессы
   self.page.tester_click_xpath('//a[@class="footer__contact"][contains(., "pressa@tvzavr.ru")]') # проверка кликабельности
   self.page.loger_info('Шаг 7. Кнопка Контакт для прессы кликабельна')
   time.sleep(1)

   self.page.waitForElementVisible('//span[@class="footer__label"][contains(., "Cлужба поддержки: ")]', 7) # найти Служба поддержки
   self.page.tester_click_xpath('//a[@class="footer__contact"][contains(., "help@tvzavr.ru")]') # проверка кликабельности
   self.page.loger_info('Шаг 8. Кнопка Служба поддержки кликабельна')
   time.sleep(1)

   self.page.waitForElementVisible('//a[@class="footer__phone"][contains(., "8 800 707 21 31")]', 7) # найти Номер телефона
   self.page.tester_click_xpath('//a[@class="footer__phone"][contains(., "8 800 707 21 31")]') # проверка кликабельности
   self.page.loger_info('Шаг 9. Кнопка с номером телефона кликабельна')
   time.sleep(1)

   self.driver.find_element_by_xpath('.//a[@class="footer__link"][contains(., "О проекте")]').click()  # Клик по ссылке о проекте
   
   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 27) # Проверка Переход на страницу О проекте
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert ('О проекте tvzavr') in res_txt # проверочное словосочетание надписи
   self.page.loger('Шаг 10. Переход на страницу "О проекте" подтвержден')
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="document__content"]', 27) # Проверка содержания страницы
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert ('e-mail: contacts@tvzavr.ru') in res_txt
   assert ('tvzavr') in res_txt
   assert ('Каталог видеофильмов') in res_txt
   assert ('Онлайн-видеотрансляция') in res_txt
   assert ('Социальные сети') in res_txt
   self.page.loger('Шаг 11. Наличие содержания текста страницы подтверждено')
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="document__links"]', 27) # Проверка наличия блока с ссылками
   res_txt = str(self.result.find_all_link("div", "document__links"))
   assert ('Вакансии') in res_txt
   assert ('Рекламодателям') in res_txt
   assert ('Правообладателям') in res_txt
   assert ('Юридическая помощь') in res_txt
   self.page.loger('Шаг 12. Наличие всех разделов в блоке ссылок подтвердено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//a[@class="document__link"][contains(., "Вакансии")]').click() # Переход в Вакансии
   time.sleep(1)
   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 5)   # Поиск заголовка страницы
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert ('Вакансии') in res_txt
   self.page.loger('Шаг 13. Переход на страницу "Вакансии" подтвержден')

   self.page.waitForElementVisible('.//div[@class="document__content"]', 10)
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert ('Работа') in res_txt
   assert ('Требования') in res_txt
   assert ('Обязанности') in res_txt
   assert ('РАЗРАБОТЧИКА') in res_txt
   assert ('PYTHON') in res_txt
   assert ('FRONTEND') in res_txt
   assert ('ANDROID') in res_txt
   assert ('QA ENGINEER') in res_txt
   assert ('Умение работать') in res_txt
   assert ('Английский язык') in res_txt
   self.page.loger('Шаг 14. Содержание страницы "Вакансии" подтверждено')
   time.sleep(1)

   self.page.waitForElementVisible('.//div[@class="document__links"]', 27) # Проверка наличия блока с ссылками на странице Вакансии
   res_txt = str(self.result.find_all_link("div", "document__links"))
   assert ('Вакансии') in res_txt
   assert ('Рекламодателям') in res_txt
   assert ('Правообладателям') in res_txt
   assert ('Юридическая помощь') in res_txt

   self.page.loger('Шаг 17. Наличие всех разделов в блоке ссылок на странице "Вакансии" подтвердено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//a[@class="document__link"][contains(., "Рекламодателям")]').click() 
   time.sleep(2)
   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 10)
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert('Рекламодателям и рекламным агентствам') in res_txt
   self.page.loger('Шаг 18. Переход на страницу "Рекламодателям" подтвержден')

   self.page.waitForElementVisible('.//div[@class="document__content"]', 10)
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert('Контактная информация:') in res_txt
   assert('Отдел рекламы') in res_txt
   assert('E-Mail: '), ('reklama@tvzavr.ru') in res_txt
   assert('Телефоны:') in res_txt
   assert('+7 495 640 1397 '), (' доб. 2023') in res_txt
   assert('+7 495 640 1397 '), (' доб. 2027') in res_txt
   self.page.loger('Шаг 19. Содержание страницы "Рекламодателям" подтверждено')
   time.sleep(2)
   
   self.page.waitForElementVisible('.//div[@class="document__links"]', 27) # Проверка наличия блока с ссылками на странице Рекламодателям
   res_txt = str(self.result.find_all_link("div", "document__links"))
   assert ('Вакансии') in res_txt
   assert ('Рекламодателям') in res_txt
   assert ('Правообладателям') in res_txt
   assert ('Юридическая помощь') in res_txt
   self.page.loger('Шаг 20. Наличие всех разделов в блоке ссылок на странице "Рекламодателям" подтверждено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//a[@class="document__link"][contains(., "Правообладателям")]').click()
   time.sleep(2)

   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 10)
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert('Правообладателям') in res_txt
   self.page.loger('Шаг 21. Переход на страницу "Правообладателям" подтверждён')
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="document__content"]', 10)
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert('Многие правообладатели') in res_txt
   assert('Платформа видеотрансляции tvzavr') in res_txt
   assert('Размещая свой видеоконтен') in res_txt
   assert('Посетите нашу '), ('Юридическую помощь правообладателю!') in res_txt
   self.page.loger('Шаг 22. Содержание на странице "Правообладателям" подтверждено')
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="document__links"]', 27) # Проверка наличия блока с ссылками на странице Рекламодателям
   res_txt = str(self.result.find_all_link("div", "document__links"))
   assert ('Вакансии') in res_txt
   assert ('Рекламодателям') in res_txt
   assert ('Правообладателям') in res_txt
   assert ('Юридическая помощь') in res_txt
   self.page.loger('Шаг 23. Наличие всех разделов в блоке ссылок на странице "Правообладателям" подтверждено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//a[@class="document__link"][contains(., "Юридическая помощь")]').click()
   time.sleep(2)

   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 10)
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert ('Некоторые юридические вопросы, связанные с использованием фильмов в сети Интернет') in res_txt
   self.page.loger('Шаг 24. Переход на страницу "Юридическая помощь" подтверждён')
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="document__content"]', 10)  # Проверка содержания страницы "Юридическая помощь"
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert ('Правообладатель') in res_txt
   assert ('права') in res_txt
   assert ('лицензия') in res_txt
   assert ('деятельности') in res_txt
   assert ('авторского') in res_txt
   self.page.loger('Шаг 25. Содержание страницы "Юридическая помощь" подтверждено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//button[@class="footer__link"][contains(., "Обратная связь")]').click()  # Клик ссылки "Обратная связь"
   time.sleep(1)

   self.page.waitForElementVisible('.//div[@class="modal__content feedback js-modal-content modal__content_open"]', 10)  # Проверка окна Обратной связи
   res_txt = str(self.result.find_all_link("div", "modal__content feedback js-modal-content modal__content_open"))
   assert ('Как мы можем вам помочь?') in res_txt
   assert ('Отправить') in res_txt
   self.page.loger('Шаг 26. Появление окна обратной связи подтверждено')

   # Проверка обратной связи
   self.page.send_f('feedback_имя_пользователя', name_user, 27)
   time.sleep(1)
    
   self.page.send_f('feedback_e_mail_пользователя', email, 28)
   time.sleep(1)
   
   self.page.send_f('feedback_сообщение_пользователя', 'Автотестирование работы обратной связи WEB tvzavr.ru', 29)
   time.sleep(2)
   
   self.page.click_f('Клик_Отправить_сообщение_обратная связь', 30)
   time.sleep(3)
   
   self.driver.execute_script("window.open('','_blank');") # открытие пустой страницы
   time.sleep(3)

   self.driver.switch_to.window(self.driver.window_handles[1])  # Переключение на вторую страницу

   self.driver.get("http://rm.tvzavr.ru/projects/helpdesk/issues")   # Переход в РэдМайн
   self.driver.implicitly_wait(10)
   time.sleep(1)
   self.driver.find_element_by_name('button').click()
   self.page.loger('Шаг 31. Переход в службу поддержки подтверждён')
   time.sleep(3)

   self.page.login_google('bykov.a@tvzavr.ru', 'tmW9HZvaksgc')
   self.page.loger('Шаг 32. Введены данные для входа')
   time.sleep(5)

   self.page.waitForElementClickable('.//table[@class="list issues odd-even sort-by-id sort-desc"]', 10)  # Поиск отправленного письма на странице службы поддержки
   res_txt = str(self.result.find_all_link("table", "list issues odd-even sort-by-id sort-desc"))
   assert ('Сообщение пользователя tvzavrtest.test@mail.ru  email:tvzavrtest.test@mail.ru') in res_txt
   self.page.loger('Шаг 33. Отправленное письмо найдено на странице службы поддержки')
   time.sleep(2)

   self.driver.close()
   time.sleep(1)
   self.driver.switch_to.window(self.driver.window_handles[-1])  # Переключение на предыдущую вкладку
   time.sleep(2)

   self.driver.find_element_by_xpath('.//a[@class="footer__link"][contains(., "Партнерам")]').click()
   time.sleep(2)
   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 10)
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert('Правообладателям') in res_txt
   self.page.loger('Шаг 34. Переход на страницу "Партнерам" подтвержден') # Больше нет проверок, т.к. страница дублирует страницу Правообладателям
   time.sleep(2)

   # Приложения вынесены в отдельный test_case_№.py

   self.driver.find_element_by_xpath('.//a[@class="footer__link"][contains(., "MoviesChain")]').click()  # Клик на ссылку MoviesChain
   self.driver.switch_to.window(self.driver.window_handles[1])   # переключение на вторую страницу
   time.sleep(2)
   
   self.page.waitForElementVisible('.//h1[@class="home-page__title home-page__title_h1"]', 10)  # Проверка заголовка на странице MoviesChain 
   res_txt = str(self.result.find_all_link("h1", "home-page__title home-page__title_h1"))
   assert('Платформа дистрибуции фильмов ') in res_txt
   self.page.loger('Шаг 35. Переход на страницу "MoviesChain" подтвержден')
   time.sleep(1)

   self.driver.close()
   time.sleep(1)
   self.driver.switch_to.window(self.driver.window_handles[-1])  # Переключение на предыдущую вкладку
   time.sleep(1)

   self.driver.find_element_by_xpath('.//a[@class="footer__link"][contains(., "Бонусная программа")]').click()
   time.sleep(1)

   self.page.waitForElementVisible('.//h1[@class="loyalty__heading superheading-1"]', 10)  # Проверка заголовка
   res_txt = str(self.result.find_all_link("h1", "loyalty__heading superheading-1"))
   assert('Смотрите фильмы —'), ('получайте бонусы!') in res_txt
   self.page.loger('Переход на страницу "Бонусная программа" подтвержден')
   time.sleep(2)

   self.page.waitForElementVisible('.//div[@class="container"]', 10)  # Проверка содержания страницы
   res_txt = str(self.result.find_all_link("div", "container"))
   assert('Получите первые 30 ₽ за регистрацию') in res_txt
   assert('Как заработать больше бонусов?') in res_txt
   assert('card card_clip') in res_txt
   self.page.loger('Шаг 36. Содержание страницы "Бонусная программа" подтверждено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//button[@class="loyalty-register__button button button_stretched"][contains(., "Зарегистрироваться")]').click() # нажать на кнопку ЗАРЕГИСТРИРОВАТЬСЯ

   self.page.waitForElementVisible('.//div[@class="modal__content login js-modal-content modal__content_open"]', 10)  # Проверка модального окна
   res_txt = str(self.result.find_all_link("div", "modal__content login js-modal-content modal__content_open"))
   assert('Вход') in res_txt
   assert('Регистрация') in res_txt
   assert('Пароль') in res_txt
   assert('Войти') in res_txt

   self.page.loger('Шаг 37. Появление и содержание окна Входа/Регистрации подтверждено')
   time.sleep(2)

   self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Закрытие модального онка кликом по крестику
   time.sleep(2)

   self.driver.find_element_by_xpath('.//a[@class="footer__link"][contains(., "Публичная оферта")]').click()
   time.sleep(2)

   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 10)
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert('Публичная оферта') in res_txt
   self.page.loger('Шаг 38. Переход на страницу "Публичная аферта" подтвержден')
   time.sleep(1)

   self.page.waitForElementVisible('.//div[@class="document__content"]', 10)  # Проверка содержания страницы
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert('Публичная оферта (предложение)'), ('об оказании услуг по использованию контента') in res_txt
   assert('г. Москва') in res_txt
   assert('услуги') in res_txt
   assert('Пользователя') in res_txt
   assert('данных') in res_txt
   self.page.loger('Шаг 39. Содержание страницы "Публичная оферта" подтверждено')
   time.sleep(1)

   self.page.click_f('Переход_вниз_страницы', 40)
   time.sleep(2)
   self.page.click_f('Переход_вниз_страницы', 40)

   self.driver.find_element_by_xpath('.//a[@class="footer__link"][contains(., "FAQ")]').click()
   time.sleep(2)

   self.page.waitForElementVisible('.//h1[@class="document__heading heading-1"]', 10)
   res_txt = str(self.result.find_all_link("h1", "document__heading heading-1"))
   assert('FAQ') in res_txt
   self.page.loger('Шаг 41. Переход на страницу "FAQ" подтвержден')

   self.page.waitForElementVisible('.//div[@class="document__content"]', 10)
   res_txt = str(self.result.find_all_link("div", "document__content"))
   assert('промокод') in res_txt
   assert('Отвязать карту') in res_txt
   assert('зарегистрироваться') in res_txt
   assert('Как удалить свой аккаунт') in res_txt
   assert('Как скачать фильм') in res_txt
   assert('tvzavr') in res_txt
   self.page.loger('Шаг 42. Содержание страницы "FAQ" подтверждено')
   time.sleep(2)

   self.driver.quit()






















   

   




   

  

   

     









   
















   #  self.page.loger('\n Запуск Тест кейс № 4 tvweb_new-4:Оплата фильма с личного счета \n Предустановка: Фильм "Малыш" должен быть в купленных фильмах \n иначе Fail')
   #  self.driver.get("https://www.tvzavr.ru:8080/admin/")

   #  time.sleep(1)  # задержка чтобы сменился логин с прошлого теста.
   #  emailt = "ttvzavr126@mail.ru"
   #  passw = '1111111'
   #  film = 'Малыш' #был film
   #  emailgo = 'bykov.a@tvzavr.ru'
   #  passok = 'tmW9HZvaksgc'
   #  # 'Открытие страницы админки

   #  self.page.loger_info('Открытие страницы админки')

   #  # Логинимся через Google
   #  self.admin.click_f('Админка_большая_красная_кнопка', 14)
   #  self.page.loger_info('Логинимся через Google')
   #  self.page.login_google(emailgo, passok)
   #  self.page.loger_info('Вошли в админку')
   #  self.driver.get("https://www.tvzavr.ru:8080/admin/tvzavr_admin/customer/68462109/tariffs_delete/")
   #  time.sleep(2)
   #  self.driver.find_elements_by_xpath('.//a[@class="delete-tariff"]')[-1].click()
   #  time.sleep(2)
   #  self.driver.find_element_by_name('desc').send_keys('test_delete')
   #  time.sleep(2)
   #  self.driver.find_element_by_xpath('//*[@id="content-main"]/form/input').click()
   #  time.sleep(2)
   #  self.driver.execute_script("window.open('','_blank');")
   #  self.driver.switch_to.window(self.driver.window_handles[1])
   #  # переключиться на новую вкладку (с индексом 1)
   #  self.driver.get("https://www.tvzavr.ru/")
   #  self.driver.implicitly_wait(2)
    
   #     # self.page.click_f('Клик_кнопки_крестик', 5) 1.08.2019
        
   #  self.page.login_tvzavr(emailt, passw)
   #  # Шаг 6
   #  #self.prof.click_f('Клик_Аватарка_М', 6) 1.08.2019
   #  # Шаг 7
   #  self.page.send_f('Ввод_2_в_строку_поиска', film, 9) 
   #  # Шаг 18
   #  self.prof.click_f('Клик_поиска_Лупа', 10)
   #  # Шаг 19
   #  self.card.click_f('Клик_иконки_найденного_фильма', 11)
   #  # Проверка перехода"
   #  #resic = str(self.result.find_link("h1", "clip_name txt-w-b txt-c-f")) 08.08.2019
   #  # Малыш - проверочное словосочетание надписи
   #  #assert ('Малыш') in resic 08.08.2019
   #  #self.page.loger_info('Переход на карточку фильма "Малыш" подтвержден') 08.08.2019
   #  # Шаг 20
   #  self.card.click_f('Клик_кнопки_просмотр_от_руб', 12)
   #  # Шаг 21
   #  # Россия
   #  self.card.click_f('Клик_кнопки_Прокат', 13)
   #  # Шаг 22
   #  self.prof.click_f('Клик_Личный_счет', 14)
   #  time.sleep(2)
   #  self.prof.click_f('Клик_Оплатить', 15)
   #  # Шаг 25
   #  self.card.click_f('Клик_Play', 16)
   #  # Шаг 26
   #  time.sleep(10)
   #  self.prof.click_f('Клик_Аватарка_М', 17)
   #  time.sleep(2)
   #  self.prof.click_f('Клик_Подписки_и_покупки', 18)
   #  self.page.waitForElementVisible('.//div[@class="clip-card__title tvz-overflow"]', 7)        # Проверка фильма малыш в купленных фильмах"
   #  resic = str(self.result.find_link("div", "clip-card__title tvz-overflow"))
   #  # email - проверочное словосочетание надписи
   #  assert ('Малыш') in resic
   #  self.page.loger_info('Наличие фильма малыш в купленных фильмах подтверждено')
   #  self.prof.click_f('Клик_Аватарка_М', 19)
   #  time.sleep(1)
   #  self.prof.click_f('Клик_Выйти', 20)

   
   
   




