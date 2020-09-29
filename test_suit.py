import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

#from Regress_web.test_case_00 import case_00 # Проигрывание рандомных фильмов циклом
### 1) Покупка/оплата
#from .test_case_1_1 import case_1_1 # Покупка фильма картой, регистрация по e-mail, проверка начисления 30р, удаление пользователя
#from .test_case_1_2 import case_1_2 # Покупка фильма с личного счета, регистрация по e-mail, проверка начисления 30р, удаление пользователя
# from .test_case_1_3 import case_1_3 # Покупка картой подписки "отключи рекламу", регистрация по e-mail, удаление
#from .test_case_1_4 import case_1_4 # Проверка пополнения личного счета с карты на 1 рубль, авторизация

### 2) Проверка фильтров
### Каталог
#from .test_case_2_1_1 import case_2_1_1 # Проверка фильтров поиска на странице Каталог(Жанры)
#from .test_case_2_1_2 import case_2_1_2 # Проверка фильтров поиска на странице Каталог(Страны)
#from .test_case_2_1_3 import case_2_1_3 # Проверка фильтров поиска на странице Каталог(Года)                 #(pyautogui)
# from .test_case_2_1_4 import case_2_1_4 # Проверка фильтров поиска на странице Каталог(Года, Жанры, Страны)  #(pyautogui)
# from .test_case_2_1_5 import case_2_1_5 # Проверка фильтров поиска на странице Каталог(Аудио)
# from .test_case_2_1_6 import case_2_1_6 # Проверка фильтров поиска на странице Каталог(Субтитры)
# from .test_case_2_1_7 import case_2_1_7 # Проверка фильтров поиска на странице Каталог(Родительский контроль)
#from .test_case_2_1_8 import case_2_1_8 # Проверка фильтров поиска на странице Каталог(Бесплатно)
### Бесплатно
# from .test_case_2_2_1 import case_2_2_1 # Проверка фильтров поиска на странице Бесплатно(Жанры)
# from .test_case_2_2_2 import case_2_2_2 # Проверка фильтров поиска на странице Бесплатно(Страны)
# from .test_case_2_2_3 import case_2_2_3 # Проверка фильтров поиска на странице Бесплатно(Года)                  #(pyautogui)
# from .test_case_2_2_4 import case_2_2_4 # Проверка фильтров поиска на странице Бесплатно(Года, Жанры, Страны)   #(pyautogui)
# from .test_case_2_2_5 import case_2_2_5 # Проверка фильтров поиска на странице Бесплатно(Аудио)
# from .test_case_2_2_6 import case_2_2_6 # Проверка фильтров поиска на странице Бесплатно(Субтитры)
# from .test_case_2_2_7 import case_2_2_7 # Проверка фильтров поиска на странице Бесплатно(Родительский контроль)
# from .test_case_2_2_8 import case_2_2_8 # Проверка фильтров поиска на странице Бесплатно(Бесплатно)
### Новинки
#from .test_case_2_3_1 import case_2_3_1 # Проверка фильтров поиска на странице Новинки(Жанры)
# from .test_case_2_3_2 import case_2_3_2 # Проверка фильтров поиска на странице Новинки(Страны)
# from .test_case_2_3_3 import case_2_3_3 # Проверка фильтров поиска на странице Новинки(Года)                 #(pyautogui)
# from .test_case_2_3_4 import case_2_3_4 # Проверка фильтров поиска на странице Новинки(Года, Жанры, Страны)  #(pyautogui)
#######from .test_case_2_3_5 import case_2_3_5 # Проверка фильтров поиска на странице Новинки(Аудио)
#######from .test_case_2_3_6 import case_2_3_6 # Проверка фильтров поиска на странице Новинки(Субтитры)
# from .test_case_2_3_7 import case_2_3_7 # Проверка фильтров поиска на странице Новинки(Родительский контроль)
# from .test_case_2_3_8 import case_2_3_8 # Проверка фильтров поиска на странице Новинки(Бесплатно)

### 3)  Проигрывание/карточка фильма
#from .test_case_3_1 import case_3_1 # Проигрывание рандомных бесплатных фильмов и взаимодействие с плеером #(pyautogui)
#from .test_case_3_2 import case_3_2 # Добавление в избранное и удаление, регистрация по e-mail, удаление
#from .test_case_3_3 import case_3_3 # Проверка элементов карточки рандомного бесплатного фильма, проигрывание и переход по похожим фильмам
#from .test_case_3_4 import case_3_4 # Проигрывание купленных фильмов, авторизация     #(pyautogui)
#from .test_case_3_5 import case_3_5 # Проигрывание сезонов сериалов
#from .test_case_3_6 import case_3_6 # Проверка кнопки "Возникла проблема?" в карточке фильма
#from .test_case_3_7 import case_3_7 # Проверка перехода в карточки фильмов в тематических подборках
#from .test_case_3_8 import case_3_8 # Проверка статуса фильмов в разделах "Подписка tvzavr +" и "Отключи рекламу на tvzavr!"

# ### 4) Соцсети/переходы
##from .test_case_4_1 import case_4_1 # Авторизация через соцсети по ссылкам из окна авторизации ТЕСТ не проходит, потому что авторизация через соц.сети работает через раз
#from .test_case_4_2 import case_4_2 # Проверка перехода по ссылкам на соцсети внизу страницы

### 5) Пользователь
# from .test_case_5_1 import case_5_1 # Настройка профиля, смена пароля, регистрация по e-mail, удаление
# from .test_case_5_2 import case_5_2 # Проверка работоспособности элементов окошка пользователя, личный кабинет, авторизация
#from .test_case_5_3 import case_5_3 # Проверка регистрации по номеру телефона и удаление пользователя  !!!КАПЧА!!!
#from .test_case_5_4 import case_5_4 # Проверка карты тройка: удаление, привязка, наличие скидки, авторизация


### 6) Переходы/работоспособность
from .test_case_6_1 import case_6_1 # Проверка работоспособности верхних разделов
#from .test_case_6_2 import case_6_2 # Проверка работоспособности нижних разделов и проверка обратной связи
#from .test_case_6_3 import case_6_3 # Проверка работоспособности вкладок и ссылок в разделе Приложения
#from .test_case_6_4 import case_6_4 # Проверка работы карты сайта
#from .test_case_6_5 import case_6_5 # Проверка добавления и удаления комментария
#from .test_case_6_6 import case_6_6 # Проверка работоспособности поиска



# from Regress_web.test_case_4 import case_4 # Проверка фильтров поиска на странице Каталог
# from Regress_web.test_case_4_2 import case_4_2 # Проверка фильтров поиска на странице Бесплатно
# from Regress_web.test_case_4_3 import case_4_3 # Проверка работоспособности кнопок "Смотреть все" с главной страницы

# from Regress_web.test_case_25 import case_25 #эксперимент
#from Regress_web.test_case_222 import case_222 #эксперимент
# from Regress_web.test_case_333 import case_333 #эксперимент
# from Regress_web.test_case_505 import case_505 #movieschain


import pytest
from .page import *


class Test():

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        ##self.driver = webdriver.Chrome(ChromeDriverManager().install())   # ЭТО НАДО ДОБАВИТЬ В ХРОМДРАЙВЕР ФЕДЕ
        #self.driver = webdriver.Chrome(r'C:\Users\abykov.RUTUBE\Documents\GitHub\smoke\chromedriver.exe') #(options=options) у меня был 78 номер 'C:/Users/Алексей Быков/Projects/qa-tests-master/Regress_web/chromedriver.exe'
        self.driver = webdriver.Chrome(r'C:\Users\abykov.RUTUBE\Desktop\driver\chromedriver.exe')  # это для дженкинса
        #################################################################self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.tvzavr.ru/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.full_screen = 0
        self.page = MainPage(self.driver)
        self.result = ResultPage(self.driver)
        self.prof = Profile(self.driver)
        self.admin = Admin(self.driver)
        self.card = CardFilm(self.driver)

    # def teardown(self):
    #     self.driver.close()

    # def test_case_00(self):
    #     case_00(self, 0)

    ### 1) Покупка/оплата
    # def test_case_1_1(self):
    #     case_1_1(self, 0)

    # def test_case_1_2(self):
    #     case_1_2(self, 0)

    # def test_case_1_3(self):
    #     case_1_3(self, 0)

    # def test_case_1_4(self):
    #     case_1_4(self, 0)

    ### 2) Проверка фильтров
    ### Каталог
    # def test_case_2_1_1(self):
    #     case_2_1_1(self, 0)

    # def test_case_2_1_2(self):
    #     case_2_1_2(self, 0)

    # def test_case_2_1_3(self):
    #     case_2_1_3(self, 0)   

    # def test_case_2_1_4(self):
    #     case_2_1_4(self, 0)    

    # def test_case_2_1_5(self):
    #     case_2_1_5(self, 0)    

    # def test_case_2_1_6(self):
    #     case_2_1_6(self, 0)    
    
    # def test_case_2_1_7(self):
    #     case_2_1_7(self, 0)    

    # def test_case_2_1_8(self):
    #     case_2_1_8(self, 0) 

    ### Бесплатно
    # def test_case_2_2_1(self):
    #     case_2_2_1(self, 0)
    #
    # def test_case_2_2_2(self):
    #     case_2_2_2(self, 0)

    # def test_case_2_2_3(self):
    #     case_2_2_3(self, 0)   

    # def test_case_2_2_4(self):
    #     case_2_2_4(self, 0)    

    # def test_case_2_2_5(self):
    #     case_2_2_5(self, 0)    

    # def test_case_2_2_6(self):
    #     case_2_2_6(self, 0)    
    
    # def test_case_2_2_7(self):
    #     case_2_2_7(self, 0)    

    # def test_case_2_2_8(self):
    #     case_2_2_8(self, 0)

    ## Новинки
    # def test_case_2_3_1(self):
    #     case_2_3_1(self, 0)

    # def test_case_2_3_2(self):
    #     case_2_3_2(self, 0)   

    # def test_case_2_3_3(self):
    #     case_2_3_3(self, 0)   

    # def test_case_2_3_4(self):
    #     case_2_3_4(self, 0)    

    ######## def test_case_2_3_5(self):
    ########   case_2_3_5(self, 0)    

    ######## def test_case_2_3_6(self):
    ########     case_2_3_6(self, 0)    
    
    # def test_case_2_3_7(self):
    #     case_2_3_7(self, 0)    

    # def test_case_2_3_8(self):
    #     case_2_3_8(self, 0)

    ### 3)  Проигрывание/карточка фильма
    # def test_case_3_1(self):
    #     case_3_1(self, 0)

    # def test_case_3_2(self):
    #     case_3_2(self, 0)

    # def test_case_3_3(self):
    #     case_3_3(self, 0)

    # def test_case_3_4(self):
    #     case_3_4(self, 0)

    # def test_case_3_5(self):
    #     case_3_5(self, 0)

    # def test_case_3_6(self):
    #     case_3_6(self, 0)

    # def test_case_3_7(self):
    #     case_3_7(self, 0)

    # def test_case_3_8(self):
    #     case_3_8(self, 0)  

    ### 4) Соцсети/переходы
    # def test_case_4_1(self):
    #     case_4_1(self, 0)

    # def test_case_4_2(self):
    #     case_4_2(self, 0)
    #
    # ### 5) Пользователь
    # def test_case_5_1(self):
    #     case_5_1(self, 0)
    #
    # def test_case_5_2(self):
    #     case_5_2(self, 0)

    # def test_case_5_3(self):
    #     case_5_3(self, 0)

    # def test_case_5_4(self):
    #     case_5_4(self, 0) 

    ### 6) Переходы/работоспособность
    def test_case_6_1(self):
        case_6_1(self, 0)

    # def test_case_6_2(self):
    #     case_6_2(self, 0)

    # def test_case_6_3(self):
    #     case_6_3(self, 0)
    #
    # def test_case_6_4(self):
    #     case_6_4(self, 0)
    #
    # def test_case_6_5(self):
    #     case_6_5(self, 0)

    # def test_case_6_6(self):
    #     case_6_6(self, 0)  
    

    




    # def test_case_11(self):
    #     case_11(self, 0)   

    # def test_case_20(self):
    #     case_20(self, 0)   

    # def test_case_25(self):
    #     case_25(self, 0)  

    # def test_case_26(self):
    #     case_26(self, 0)  

    # def test_case_222(self):
    #     case_222(self, 0) 

    # def test_case_333(self):
    #     case_333(self, 0) 

    # def test_case_4(self):
    #     case_4(self, 0)

    # def test_case_4_2(self):
    #     case_4_2(self, 0)

    # def test_case_4_3(self):
    #     case_4_3(self, 0)

    # def test_case_505(self):
    #     case_505(self, 0)