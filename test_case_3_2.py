from .page import * 

time.sleep(2)
def case_3_2(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 3_2 tvweb_new-3_2: Проверка добавления фильма в избранное и удаление  \n')
    
    email = self.page.rand_mail('8')[0]
    passw = '333333'

    self.page.click_f('Клик_Вход', 1)
    time.sleep(1)
    self.prof.click_f('Клик_Регистрация', 2)
    time.sleep(2)

    #self.page.send_f('Ввод_логина', email, 3)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__address textbox"]').send_keys(email)
    time.sleep(2)

    #self.page.send_f('Ввод_пароля', passw, 4)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__password textbox"]').send_keys(passw)
    time.sleep(2)

    self.prof.click_f('Клик_Зарегистрироваться', 3)
    time.sleep(8)
    
    self.prof.click_f('Клик_значок_нового_пользователя', 4)
    time.sleep(2)

    remember_name = self.driver.find_element_by_xpath("//div[@class='profile-menu__name __username']") # запоминание имени пользователя
    remember_name = remember_name.get_attribute('innerHTML')
    text = remember_name
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 10)  # Проверка авторизации пользователя
    time.sleep(1)
    resic = str(self.result.find_link("div", "profile-menu__name __username")) 
    time.sleep(1)
    assert (email) in resic   # проверочное словосочетание надписи
    time.sleep(1)
    self.page.loger('Авторизация зарегистрированного пользователя с е-майлом ' + email + ' подтверждена')
    time.sleep(2)

    self.prof.click_f('Клик_мои_фильмы', 5)
    time.sleep(5)
    self.prof.click_f('Клик_крестик_всплывшего_окна_тройка', 6)
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="empty-list__heading"][contains(., "Здесь будут все ваши фильмы")]', 9) # проверка на отсутствие фильмов в избранном
    time.sleep(1)
    resic = str(self.result.find_all_link("div", "empty-list__heading"))
    time.sleep(1)
    assert ('Здесь будут все ваши фильмы') in resic # проверочное словосочетание надписи
    time.sleep(1)
    self.page.loger('Отсутствие фильмов в избранном подтверждено')
    time.sleep(2)

    self.page.click_f('Клик_Бесплатно', 7)
    time.sleep(3)
    self.page.click_f('Клик_постер_первого_фильма', 8)
    time.sleep(4)
    
    target = self.driver.find_element_by_xpath('.//div[@class="clip__actions"]') # элемент блок с постером и ссылками
    time.sleep(2)
    target.location_once_scrolled_into_view  # скролл до элемента блок с постером и ссылками
    time.sleep(1)

    self.card.click_f('Клик_кнопки_В_избранное', 9)
    time.sleep(3)
    
    self.prof.click_f('Клик_значок_пользователя', 10) 
    time.sleep(3)

    self.prof.click_f('Клик_мои_фильмы', 11)
    time.sleep(5)
    
    self.page.waitForElementVisible('.//div[@class="selection__heading heading-2"][contains(., "Избранное")]', 10) # поиск раздела избранное
    resic = str(self.result.find_all_link("div", "cabinet__container")) 
    assert ('Избранное') in resic   
    time.sleep(2)
    self.page.loger('появление раздела Избранное подтверждено')   # то есть, проверка для того,что когда не добавлен фильм в избранное, самого раздела тоже нет
    time.sleep(2)

    self.page.waitForElementVisible('.//a[@class="card card_clip"]', 10)   # весь блок фильма
    self.page.loger('нахождение фильма в избранном подтверждено')
    time.sleep(1)

    self.page.waitForElementVisible('.//div[@class="card__poster"]', 10)   # постер фильма
    self.page.loger('наличие постера фильма подтверждено')
    time.sleep(1)

    res_txt = str(self.result.find_link("div", "card__title").text)  # название фильма
    self.page.loger('Наличие названия фильма: "' + res_txt.strip() + '" подтверждено')
    time.sleep(1)   

    res_txt = str(self.result.find_link("div", "card__rating rating").text)  # наличие рейтинга
    self.page.loger('Наличие рейтинга фильма: "' + res_txt.strip() + '" подтверждено')
    time.sleep(1)

    res_txt = str(self.result.find_link("div", "card__label card__label_free").text)  # платно/бесплатно
    self.page.loger('статус фильма: "' + res_txt.strip() + '" подтвержден')
    time.sleep(2)

    self.page.click_f('Клик_постер_первого_фильма', 12)
    time.sleep(5)
    target = self.driver.find_element_by_xpath('.//div[@class="clip__actions"]') # элемент блок с постером и ссылками
    time.sleep(1)
    target.location_once_scrolled_into_view  # скролл до элемента target
    time.sleep(2)

    self.card.click_f('Клик_кнопки_Убрать_из_избранного', 13)
    time.sleep(4)

    self.prof.click_f('Клик_значок_пользователя', 14)
    time.sleep(4)

    self.prof.click_f('Клик_мои_фильмы', 15)
    time.sleep(5)

    self.page.waitForElementVisible('.//div[@class="page__container"]', 15)  # Проверка отсутствия раздела Избранное
    resic = str(self.result.find_all_link("div", "page__container"))
    assert ('Избранное') not in resic, "Раздел избранное не скрыт после удаления фильма"
    self.page.loger('Раздел Избранное скрылся после удаления фильма')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="empty-list__heading"][contains(., "Здесь будут все ваши фильмы")]', 20)  # Проверка наличия надписи "Здесь будут все ваши фильмы"
    resic = str(self.result.find_all_link("div", "empty-list__heading"))
    assert ('Здесь будут все ваши фильмы') in resic, "Название раздела 'Здесь будут все ваши фильмы' отсутствует"
    self.page.loger('Наличие раздела "Здесь будут все ваши фильмы" подтверждено')
    time.sleep(2)
       
    self.page.waitForElementVisible('.//div[@class="page__container"]', 20)  # Проверка отсутствия фильмов в контейнере страницы
    resic = str(self.result.find_all_link("div", "page__container"))
    assert ('card card_clip') not in resic, "фильм не удалился"
    
    self.page.loger('Удаление фильма из "Избранного" подтверждено')

    self.prof.click_f('Клик_значок_пользователя', 16)
    time.sleep(1)

    self.prof.click_f('Клик_Выйти', 17)
    time.sleep(1)

    self.page.delete_uzer(remember_name)
    self.page.loger('Пользователь ' + remember_name + ' удален')
    time.sleep(2)

    self.driver.quit()