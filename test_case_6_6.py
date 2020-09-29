from .page import * 

time.sleep(3)
def case_6_6(self, full_screen):
    self.page.loger('\n Запуск Тест кейс № 6_6 tvweb_new-6_6: Проверка работоспособности поиска \n')

    
    full_name = ["Стэн и Олли", "Зеленая книга", "Сфера", "Он и она", "Оно 2", "Зубная фея", "Остров собак", "Суперсемейка 2",
    "Фаворитка", "Закатать в асфальт", "Аквамен", "Талли", "Веном", "Смолфут", "Не в себе", "Кислота", "22 мили", "Патрик",
    "Trench", "Операция шаровая молния", "Папа-мама гусь", "Астрал 4: Последний ключ", "Щегол", "Кадавр", "Кодекс Готти",
    "Сокровище ермака", "Три билборда", "Дюнкерк", "Одаренная", "Дуэлянт", "Форма воды", "Джуманджи", "Бамблби", "Репродукция",
    "Капкан", "Не верь никому", "Между рядами", "Красный воробей", "Лукас", "Не попадись", "Два хвоста", "Заповедник", "Великий уравнитель 2",
    "Игры джентльменов", "Дамбо", "Хищник", "Моана","Дюймовочка", "Форрест Гамп", "Армагеддон", "Король лев"]

    m = random.randint(0, 50)
    a = random.randint(0, 50)
    b = random.randint(0, 50)
    c = random.randint(0, 50)
    d = random.randint(0, 50)
    e = random.randint(0, 50)
    f = random.randint(0, 50)
    g = random.randint(0, 50)
    h = random.randint(0, 50)
    
    movie = full_name[m]
    movie2 = full_name[a]
    movie3 = full_name[b]
    movie4 = full_name[c]
    movie5 = full_name[d]
    movie6 = full_name[e]
    movie7 = full_name[f]
    movie8 = full_name[g]
    movie9 = full_name[h]
    
    time.sleep(3)
    self.page.loger('Шаг 1. Проверка поиска на главной странице')
    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie)]', 45)
    self.page.loger('фильм: "' + movie + '" найден')
    time.sleep(3)
    
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------
    
    self.page.click_f('Клик_Новинки', 2)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie2) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie2)]', 45)
    self.page.loger('фильм: "' + movie2 + '" найден')
    time.sleep(3)
    
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------

    self.page.click_f('Клик_Подписки', 3)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie3) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie3)]', 45)
    self.page.loger('фильм: "' + movie3 + '" найден')
    time.sleep(3)
        
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------

    self.page.click_f('Клик_Бесплатно', 4)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie4) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie4)]', 45)
    self.page.loger('фильм: "' + movie4 + '" найден')
    time.sleep(3)
        
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------

    self.page.click_f('Клик_Подборки', 5)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie5) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie5)]', 45)
    self.page.loger('фильм: "' + movie5 + '" найден')
    time.sleep(3)
        
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------

    self.page.click_f('Клик_Каталог', 6)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie6) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie6)]', 45)
    self.page.loger('фильм: "' + movie6 + '" найден')
    time.sleep(3)
        
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------

    self.page.click_f('Клик_Детям', 7)
    time.sleep(4)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie7) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie7)]', 45)
    self.page.loger('фильм: "' + movie7 + '" найден')
    time.sleep(3)
        
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
    #----------------------------------------------------------------

    self.page.click_f('Клик_Спецпроекты', 8)
    time.sleep(3)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').send_keys(movie8) # ввод рандомного названия в поиск
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="header-search__button"]').click() # клик поиск
    self.page.waitForElementVisible('.//div[@class="modal__content search js-modal-content modal__content_open"]', 45) # ожидание появления контейнера поиска 20 сек
    time.sleep(3)
    self.page.waitForElementVisible('.//div[@class="search-clip__title subheading-1"][contains (., movie8)]', 45)
    self.page.loger('фильм: "' + movie8 + '" найден')
    time.sleep(3)
        
    self.driver.find_element_by_xpath('.//button[@class="modal__close"]').click() # клик крестик на странице поиска
    time.sleep(2)

    self.driver.find_element_by_xpath('.//input[@class="header-search__field"]').clear() # очистить поле ввода
    time.sleep(2)
        
    self.driver.quit()