from .page import * 

def case_6_3(self, full_screen):

    self.driver.get("https://www.tvzavr.ru/")
    self.page.loger_info('\n Тест кейс № 6_3 tvweb_new-6_3: Проверка ссылок и вкладок в разделе Приложения \n')
    time.sleep(1)

    self.page.click_f('Переход_вниз_страницы', 1)
    time.sleep(3)
    self.page.click_f('Переход_вниз_страницы', 2)
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@href="/apps/"]').click() # Клик раздел Приложения
    time.sleep(2)

    self.page.loger('Шаг 3. Переход на вкладку "Smart TV"')
    self.page.waitForElementVisible('.//h1[@class="apps__heading superheading-1"]', 10)
    res_txt = str(self.result.find_link("h1", "apps__heading superheading-1"))
    assert('Смотри tvzavr'), ('на любых устройствах') in res_txt
    self.page.loger('Переход на вкладку "Smart TV" потвержден')
    time.sleep(2)

    self.page.loger('Шаг 4. Проверка наличия содержания страницы')
    self.page.waitForElementVisible('.//div[@class="apps__content apps-smart"]', 10)  # Проверка наличия текста
    res_txt = str(self.result.find_link("div", "apps__content apps-smart"))
    assert('Выбери модель своего телевизора') in res_txt
    assert('Для привязки устройств следуй инструкции') in res_txt
    self.page.loger('Наличие содержания подтверждено')
    time.sleep(2)

    self.page.loger('Шаг 5. Проверка инструкции LG WebOS')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-lg-after2015"]').click()  # Клик на LG WebOS 
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('LG WebOS'), ('2015') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('1. В поиске написать «tvzavr» и открыть приложение') in res_txt
    assert('2. Нажать «Установить», а затем «Запустить»') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как переместить приложение в удобное место') in res_txt
    assert('1. В нижнем меню нажать кнопку «Карандаш» (в самом конце)') in res_txt
    assert('2. Выбрать приложение «tvzavr» и нажать «ОК»') in res_txt
    assert('3. Перенести в удобное место и нажать «ОК»') in res_txt
    assert('Теперь Вы сможете быстро найти Ваше любимое приложение!') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('1. В приложении перейти в раздел «Профиль»') in res_txt
    assert('2. Ввести логин и пароль') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции LG WebOS подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    self.page.loger('Шаг 6. Проверка инструкции LG NetCast')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-lg-until2015"]').click() # Клик на LG NetCast
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('LG NetCast'), ('2015') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('2. Нажать «Установить», а затем «Запустить»') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как переместить приложение в удобное место') in res_txt
    assert('1. В правом верхнем углу нажать кнопку «Изменить» (карандаш)') in res_txt
    assert('2. Выбрать приложение «tvzavr» и нажать «Переместить»') in res_txt
    assert('3. Перенести в удобное место и нажать «ОК»') in res_txt
    assert('Теперь Вы сможете быстро найти Ваше любимое приложение!') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции LG NetCast подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    # Инструкция Samsung Tizen TV
    self.page.loger('Шаг 7. Проверка инструкции Tizen TV')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-samsung-tizen-after2015"]').click() # Клик на Samsung Tizen TV
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('Samsung Tizen'), ('2015') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('1. В поиске написать «tvzavr» и открыть приложение') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как переместить приложение в удобное место') in res_txt
    assert('1. Перейти в раздел «Apps» и выбрать «tvzavr»') in res_txt
    assert('2. Нажать стрелку «^» и выбрать «Добавить на главный экран»') in res_txt
    assert('3. Нажать стрелку «↓» и выбрать «Переместить»') in res_txt
    assert('4. Перенести в удобное место и нажать «ОК»') in res_txt
    assert('Теперь Вы сможете быстро найти Ваше любимое приложение!') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('1. В приложении перейти в раздел «Профиль»') in res_txt
    assert('2. Ввести логин и пароль') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции Samsung Tizen TV подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    # Инструкция Samsung Orsay TV
    self.page.loger('Шаг 8. Проверка инструкции Samsung Orsay TV')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-samsung-orsay-until2015"]').click() # Клик на Samsung Orsay TV
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('Samsung Orsay'), ('2015') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('1. Открыть приложение и перейти в раздел «Видео»') in res_txt
    assert('2. Выбрать приложение «tvzavr»') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как переместить приложение в удобное место') in res_txt
    assert('1. Нажать стрелку «^» и выбрать «Закрепить»') in res_txt
    assert('2. После этого приложение станет первым в списке') in res_txt
    assert('Теперь Вы сможете быстро найти Ваше любимое приложение!') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('1. В приложении перейти в раздел «Профиль»') in res_txt
    assert('2. Ввести логин и пароль') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции Samsung Orsay TV подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    # Инструкция Sony Android TV
    self.page.loger('Шаг 9. Проверка инструкции Sony Android TV')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-sony-android-after2015"]').click() # Клик на Sony Android TV
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('Sony Android'), ('2015') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('1. Открыть Google Play и в поиске написать «tvzavr»') in res_txt
    assert('2. Открыть приложение и нажать «Установить»') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('1. В приложении перейти в раздел «Профиль»') in res_txt
    assert('2. Ввести логин и пароль') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции Sony Android TV подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)


    # Инструкция Sony Linux
    self.page.loger('Шаг 10. Проверка инструкции Sony Linux')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-sony-linux-after2013"]').click() # Клик на Sony Linux
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('Sony Linux'), ('2013') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('1. В приложении перейти в раздел «Профиль»') in res_txt
    assert('2. Ввести логин и пароль') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции Sony Linux подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    # Инструкция Panasonic
    self.page.loger('Шаг 11. Проверка инструкции Panasonic')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-panasonic"]').click() # Клик на Panasonic
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('Panasonic') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('1. Открыть Apps Market и перейти в раздел «Видео»') in res_txt
    assert('2. Найти приложение «tvzavr» и нажать «Бесплатно»') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как переместить приложение в удобное место') in res_txt
    assert('1. В правом верхнем углу нажать кнопку «Настройки»') in res_txt
    assert('2. Выбрать «Переместить приложение»') in res_txt
    assert('3. Выбрать приложение «tvzavr» и перенести в удобное место') in res_txt
    assert('Теперь Вы сможете быстро найти Ваше любимое приложение!') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции Panasonic подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    # Инструкция Philips
    self.page.loger('Шаг 12. Проверка инструкции Philips')
    self.driver.find_element_by_xpath('.//button[@data-modal="apps-smart-philips"]').click() # Клик на Panasonic
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="modal__content apps-info js-modal-content modal__content_open"]', 10) # Ожидание появления инструкции и проверка её содержания
    res_txt = str(self.result.find_link("div", "modal__content apps-info js-modal-content modal__content_open"))
    assert('Philips') in res_txt
    assert('Инструкция по установке приложения') in res_txt
    assert('1. В поиске ввести «tvzavr»') in res_txt
    assert('2. Выбрать приложение и нажать «Добавить»') in res_txt
    assert('Теперь приложение находится в нижнем меню') in res_txt
    assert('Как переместить приложение в удобное место') in res_txt
    assert('1. Выбрать приложение «tvzavr» и нажать «Переместить» (зеленая кнопка)') in res_txt
    assert('2. Перенести в удобное место и нажать «ОК»') in res_txt
    assert('Теперь Вы сможете быстро найти Ваше любимое приложение!') in res_txt
    assert('Как авторизоваться') in res_txt
    assert('1. В приложении перейти в раздел «Профиль»') in res_txt
    assert('2. Ввести логин и пароль') in res_txt
    assert('3. Если нет учетной записи, то нужно нажать «Регистрация»') in res_txt
    assert('Теперь все Ваши покупки и подписки доступны на Smart TV!') in res_txt
    self.page.loger('Содержание инструкции Philips подтверждено')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click()  # Клик крестик на инструкции
    time.sleep(2)

    # Проверка содержания страницы Smart TV
    self.page.loger('Шаг 13. Проверка содержания страницы Smart TV')
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="apps-smart__section apps-smart__section_1"]', 10)
    res_txt = str(self.result.find_link("div", "apps-smart__section apps-smart__section_1"))
    assert('Дома как в кино со Smart TV') in res_txt
    assert('Как найти и запустить приложение для Smart TV читай в нашей инструкции.') in res_txt
    assert('Фильмы в Full HD и 4K') in res_txt
    assert('Картинка всегда стабильна, не требуется ждать загрузку') in res_txt

    self.page.waitForElementVisible('.//div[@class="apps-smart__section apps-smart__section_2"]', 10)
    res_txt = str(self.result.find_link("div", "apps-smart__section apps-smart__section_2"))
    assert('Удобный поиск кино') in res_txt
    assert('Показ автоматически продолжается с того момента, где остановился в прошлый раз.') in res_txt

    self.page.waitForElementVisible('.//div[@class="apps-smart__cartoons info-block info-block info-block_flip"]', 10)
    res_txt = str(self.result.find_link("div", "apps-smart__cartoons info-block info-block info-block_flip"))
    assert('Огромный выбор мультфильмов') in res_txt
    assert('Включив «Родительский контроль», ребенок может сам выбрать мультфильм по своему возрасту.') in res_txt
    self.page.loger('Содержание страницы Smart TV подтверждено')

    # Проверка раздела "Мобильные устройства"
    self.page.loger('Шаг 14. Проверка содержания страницы "Мобильные устройства"')

    self.driver.find_element_by_xpath('.//a[@data-target="apps-mobile"]').click() # Клик на мобильные устройства
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="tvz-tab_content"]', 10)
    res_txt = str(self.result.find_link("div", "tvz-tab_content"))
    assert('tvzavr для iOS') in res_txt
    assert('мы собрали всё самое лучшее в приложении tvzavr.') in res_txt
    assert('tvzavr для Android') in res_txt
    assert('советские мультфильмы и свежие премьеры западных сериалов – для взрослых и детей.') in res_txt
    self.page.loger('Содержание страницы "Мобильные устройства" подтверждено')
    time.sleep(2)

    self.page.loger('Шаг 15. Проверка ссылок на App Store и Google Play')
    time.sleep(1)

    # App Store
    self.page.loger('1.Проверка перехода в App Store')
    self.driver.find_element_by_xpath('.//a[@href="https://itunes.apple.com/ru/app/интернет-кинотеатр-tvzavr-2-0/id1376531508"]').click() # Клик на ссылку App Store
    self.driver.switch_to.window(self.driver.window_handles[1]) # Переключение на вторую вкладку
    time.sleep(2)
    
    url1 = self.driver.current_url    # Получение url
    if url1 == 'https://apps.apple.com/ru/app/%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82-%D0%BA%D0%B8%D0%BD%D0%BE%D1%82%D0%B5%D0%B0%D1%82%D1%80-tvzavr-2-0/id1376531508':
        self.page.loger('Переход по ссылке в "App Store" подтверждён')
    else:
        assert(), "Переход в App Store не произведён"
    time.sleep(2)

    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    # Google Play
    self.page.loger('2.Проверка перехода в Google Play')
    self.driver.find_element_by_xpath('.//a[@href="https://play.google.com/store/apps/details?id=com.tvzavr.app.android"]').click() # Клик на ссылку Google Play
    self.driver.switch_to.window(self.driver.window_handles[1]) # Переключение на вторую вкладку
    time.sleep(2)
    
    url1 = self.driver.current_url    # Получение url
    if url1 == 'https://play.google.com/store/apps/details?id=com.tvzavr.app.android':
        self.page.loger('Переход в "Google Play" подтверждён')
    else:
        assert(), "Переход в Google Play не произведён"
    time.sleep(2)

    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    # Проверка вкладки "Медиаплееры"
    self.page.loger('Шаг 16. Проверка вкладки "Медиаплееры" и переход на сайты медиаплееров')
    self.driver.find_element_by_xpath('.//a[@href="/apps/mediaplayer"]').click() # Клик на вкладку Медиаплееры
    time.sleep(2)

    # # Dune
    self.page.loger('1.Проверка перехода на сайт медиаплеера Dune')
    self.driver.find_element_by_xpath('.//a[@href="http://www.dune.ru/"]').click() # Клик на Dune HD
    time.sleep(2)

    self.driver.switch_to.window(self.driver.window_handles[1]) # Переключение на вторую вкладку
    time.sleep(2)
    
    url1 = self.driver.current_url    # Получение url
    if url1 == 'http://www.dune.ru/':
        self.page.loger('Переход на сайт медиаплеера Dune подтверждён')
    else:
        assert(), "Переход на сайт медиаплеера Dune не произведён"
    time.sleep(2)

    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    # Rombica
    self.page.loger('2.Проверка перехода на сайт медиаплеера Rombica')
    self.driver.find_element_by_xpath('.//a[@href="http://rombica.ru/catalog/smart-tv/"]').click() # Клик на Rombica
    time.sleep(4)

    self.driver.switch_to.window(self.driver.window_handles[1]) # Переключение на вторую вкладку
    time.sleep(3)
    
    url1 = self.driver.current_url    # Получение url
    if url1 == 'http://rombica.ru/category_product/player/':
        self.page.loger('Переход на сайт медиаплеера Rombica подтверждён')
    else:
        assert(), "Переход на сайт медиаплеера Rombica не произведён"
    time.sleep(2)

    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    # Eltex
    self.page.loger('3.Проверка перехода на сайт медиаплеера Eltex')
    self.driver.find_element_by_xpath('.//a[@href="http://eltex.nsk.ru/"]').click() # Клик на Eltex
    time.sleep(2)

    self.driver.switch_to.window(self.driver.window_handles[1]) # Переключение на вторую вкладку
    time.sleep(2)
    
    url1 = self.driver.current_url    # Получение url
    if url1 == 'https://eltex-co.ru/':
        self.page.loger('Переход на сайт медиаплеера Eltex подтверждён')
    else:
        assert(), "Переход на сайт медиаплеера Eltex не произведён"
    time.sleep(2)

    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    self.driver.find_element_by_xpath('.//a[@data-target="apps-smart"]').click()
    time.sleep(2)

    self.driver.quit()


    





    
