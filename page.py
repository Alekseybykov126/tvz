#import requests
from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import logging
from .page import *
#import pyautogui
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.remote.command import Command
import time
from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
from time import sleep
from sys import exit
import random

SLEEP_SHORT = 10
SLEEP_MEDIUM = 15
SLEEP_LONG = 20


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class ResultPage(BasePage):
    def find_link(self, tag_, class_):
        """ Найти подтверждающий элемент
        """
        page = MainPage(self.driver)
        path = './/ttag[@class="cclass"]'
        path_1 = path.replace('ttag', tag_)
        xpath = path_1.replace('cclass', class_)
        # page.waitForElementVisible(xpath, 7)
        time.sleep(SLEEP_SHORT)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        # print('Это суп', soup)
        ls = soup.find(tag_, class_)
        # print(ls)
        return ls

    def find_all_link(self, tag_, class_):
        "List of links"
        page = MainPage(self.driver)
        path = './/ttag[@class="cclass"]'
        path_1 = path.replace('ttag', tag_)
        xpath = path_1.replace('cclass', class_)
        page.waitForElementVisible(xpath, 7)
        time.sleep(SLEEP_SHORT)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        ts = soup.find_all(tag_, class_)
        # print(ts)
        return ts

    def find_x(self, tag_, class_):   # слайды
        #print(self, tag_, class_) закомментил, потому что выводит ненужную строчку символов
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        ts = soup.find(tag_, class_)
        ls = ts.find('a').get('clip_name')  #это дочь, в test_case_1 указывается родитель
        # print(ls)
        return ls

    def find_y(self, tag_, class_):   # год1
        print(self, tag_, class_)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        ts = soup.find(tag_, class_)
        ls = ts.find('button').get('filter__item filter__item_year').getText()
        # print(ls)   '//button[text()="Outliers"]'
        return ls

    def find_n(self, tag_, class_):   # год2
        print(self, tag_, class_)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        ts = soup.find(tag_, class_)
        ls = ts.find('button').get('years-to').getText()
        # print(ls)
        return ls

    def find_tag(self, tag_):
        # print(self, tag_, class_)
        time.sleep(SLEEP_LONG)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        # print('Это суп', soup)
        ls = soup.find(tag_)
        # print(ls)
        return ls

    def find_all_tag(self, tag_):
        # print(self, tag_, class_)
        time.sleep(SLEEP_SHORT)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        # print('Это суп', soup)
        ls = soup.find_all(tag_)
        # print(ls)
        return ls

    def simple_find(self, xpath, number):
        ls = self.driver.find_elements_by_xpath(xpath)[number]
        # print(ls)
        return ls

    def visible_xpath(self, xpath):
        time.sleep(SLEEP_SHORT)
        return EC.presence_of_element_located((By.XPATH, xpath))


class Admin(BasePage):

    def click_f(self, name, stap):
        page = MainPage(self.driver)
        step = str(stap)
        self.adminx = {
            'Клик_In_Progress_статус': {'func':page.click_xpath, 'path':'//*[@id="issue_status_id"]/option[4]'},
            'Клик_удалить_фильм_Малыш': {'func': page.click_xpath, 'path': './/a[text()="Прокат фильма (QA version)"]'},
            #'Клик_подтвердить': {'func':page.click_a}
            'Клик_Принять': {'func':page.click_xpath, 'path':'.//*[@id="issue-form"]/input[6]'},
            'Клик_Ответить': {'func':page.click_xpath, 'path':'.//span[@class="b-letter__foot__tab"]'},
            'Клик_Отправить_письмо': {'func':page.click_xpath, 'path':'//*[@id="b-toolbar__right"]/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/span'},
            'Клик_Входящие_mail_ru': {'func':page.click_xpath, 'path':'//*[@id="b-nav_folders"]/div/div[1]'},
            'Клик_Чекбокс_Входящие_mail_ru': {'func':page.click_xpath, 'path':'.//div[@class="b-checkbox__box"]'},
            'Клик_Удалить_письма_из_mail_ru': {'func':page.click_xpath, 'path':'//*[@id="b-toolbar__right"]/div[2]/div/div[2]/div[2]/div/div[1]/span'},
            'Клик_список_статус':{'func':page.click_id, 'path':'issue_status_id'},
            'Админка_клик_найти':{'func':page.click_id, 'path':'id-submit-search'},
            'Админка_клик_чекбокс_1':{'func':page.click_id, 'path':'action-toggle'},
            'Админка_Действие':{'func':page.click_name, 'path':'action'},
            'Админка_Выбор_Удалить_пользователя':{'func':page.click_css, 'path':'#action_block > label > select > option:nth-child(14)'},
            'Админка_Выполнить':{'func':page.click_name, 'path':'index'},
            #'Админка_подтвердить':{'func':page.click_css, 'path':'#content-main > form > input[type="submit"]'}, 
            'Админка_подтвердить':{'func':page.click_xpath, 'path':'//input[@value="Да, я уверен"]'},
            'Админка_большая_красная_кнопка':{'func':page.click_css, 'path':'body > div > section > a'},
            'Клик_первое_письмо': {'func': page.click_xpath, 'path': './/a[@class="js-href b-datalist__item__link"]'},
            'Клик_второе_письмо': {'func': page.click_s_xpath, 'path': './/a[@class="js-href b-datalist__item__link"]', 'index':1},
            'Переключение_1_в_iframe': {'func': page.click_switch_to, 'path': 'iframe', 'index':1},
            'Возврат_фокуса_из_iframe': {'func': page.driver.switch_to.default_content, 'path': 'None'},
            'Клик_Closed_статус': {'func': page.double, 'path_1': '//*[@id="issue_status_id"]/option[7]', 'path_2': './/option[@value="5"]'},
            #'Профили_посетителей': {'func': page.click_xpath, 'path': './/a[text()="Профили посетителей"]'},
            'Профили_посетителей': {'func': page.click_xpath, 'path': './/a[@href="/admin/tvzavr_admin/customer/"]'},

        }
        #'': {'func': '', 'path': ''}
        self.args = self.adminx[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
# эти клики еще не внесены в словарь (((

class CardFilm(BasePage):

    def click_f(self, name, stap):
        page = MainPage(self.driver)
        step = str(stap)
        self.cardx = {
            'Клик_кнопки_просмотр_от_руб': {'func': page.click_xpath, 'path': './/button[@class="clip-player__action button"]'},
            'Клик_кнопки_напрокат_SD-10р': {'func': page.click_xpath, 'path': './/button[@class="tariffs__buy js-payment-info"]'},
            'Клик_кнопки_напрокат_SD-11.88р': {'func': page.click_xpath, 'path': './/button[@data-tariff-id="575"]'},
            'Клик_Личный_счёт': {'func': page.click_xpath, 'path': './/a[@class="tabs__link js-tabs-link"][contains(., "Личный счёт")]'},
            'Клик_Оплатить_личный_счет': {'func': page.click_xpath, 'path': './/button[@class="payment-cloudpayments__card button button_stretched js-buy-button"]'},
            'Клик_кнопки_В_избранное': {'func': page.click_xpath, 'path': './/button[@class="clip__action"]'},
            'Клик_кнопки_Убрать_из_избранного': {'func': page.click_xpath, 'path': './/button[@class="clip__action clip__action_active"]'},
            #'Клик_кнопки_Прокат': {'func': page.click_xpath, 'path': './/span[@class="tvz-currency tvz-currency-RUB"]'},
            'Клик_иконки_найденного_фильма': {'func': page.click_xpath, 'path': './/a[@href="/film/lunnyi-kamen/"]'}, 
            'Клик_первого_фильма': {'func': page.click_xpath, 'path': './/a[@class="card card_clip"]'},
            'Клик_иконки_избранного_фильма': {'func': page.click_xpath, 'path': './/div[@class="clip-card__title tvz-overflow"]'},
            'Клик_иконки_фильма_в_избранном': {'funk': page.click_xpath, 'path': './/a[@class="card card_clip"]'},
            'Клик_Play': {'func': page.click_xpath, 'path': '//div[@class="tvz-button tvz-bpb2"]'},
            'Клик_пауза': {'func': page.click_xpath, 'path': '//div[@class="tvz-button tvz-button_play"]'},
            'Клик_вкладки_Описание': {'func': page.click_xpath, 'path': '//h2[@class="clip__subheading"][contains(., "Описание")]'},
            #'Клик_вкладки_Комментарии': {'func': page.click_xpath, 'path': '//*[@id="page-content"]/div[2]/div[2]/div[4]/div/ul/li[4]/a'},
            'Клик_вкладки_Серии': {'func': page.click_xpath, 'path': '//h2[@class="clip__subheading"][contains(., "Серии")]'},
            'Клик_2_ой_Серии_1_го_сезона': {'func': page.click_xpath, 'path': '//div[@class="series-card__title"][contains(., "2 серия")]'},
            'Клик_на_вкладку_Отзывы ': {'func': page.click_xpath, 'path': './/a[@data-target="clip-comments"]'},
            'Клик_на_вкладку_Трейлеры': {'func': page.click_xpath, 'path': '//a[@data-target="clip-trailers"]'},
            'Клик_на_вкладку_Награды': {'func': page.click_xpath, 'path': '//a[@data-target="clip-awards"]'},
            'Клик_на_вкладку_описание': {'func': page.click_xpath, 'path': '//a[@data-target="clip-info"]'},
             #'': {'func': '', 'path': ''} 
        }
        self.args = self.cardx[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')

class Profile(BasePage):
    def click_f(self, name, step_int):
        result = ResultPage(self.driver)
        page = MainPage(self.driver)
        step = str(step_int)
        self.profx = {
            'Клик_Зарегистрироваться': {'func': page.click_id, 'path': 'email-registration-submit'},
            'Клик_поиска_Лупа': {'func': page.click_id, 'path': 'header-search-button'},
            'Клик_Подписки': {'func': page.click_xpath, 'path': './/a[@class="profile-menu__link"][contains(., "Подписки")]'}, #подписке в значке профиля
            'Клик_Выйти': {'func': page.click_xpath, 'path': './/button[@class="profile-menu__logout js-profile-logout"]'},
            'Клик_Пополнить': {'func': page.click_xpath, 'path': './/button[@class="cabinet-balance__replenish button button_stretched js-replenishment"]'}, 
            'Клик_Личный_счет': {'func': page.click_xpath, 'path': './/a[@class="profile-menu__link"][contains(., "Счет")]'},
            'Клик_Личный_счет_нового_пользователя': {'func': page.click_xpath, 'path': './/a[@class="profile-menu__link profile-menu__link_notified"][contains(., "Счет")]'},
            'Клик_Регистрация': {'func': page.click_xpath, 'path': './/a[text()="Регистрация"]'},
            'Клик_phone_Зарегистрироваться': {'func': page.click_css, 'path': '#register-submit'},
            'Клик_значок_пользователя': {'func': page.click_xpath, 'path': './/button[@class="header__profile  js-profile-menu"]'},
            'Клик_значок_нового_пользователя': {'func': page.click_xpath, 'path': './/button[@class="header__profile header__profile_notified js-profile-menu"]'},
            'Клик_мои_фильмы': {'func': page.click_xpath, 'path': './/a[@class="profile-menu__link"][contains(., "Мои фильмы")]'},
            'Клик_крестик_всплывшего_окна_тройка': {'func': page.click_xpath, 'path': './/button[@class="modal__close"]'},
            'Клик_Настройки_профиля': {'func': page.click_xpath, 'path': './/a[@class="profile-menu__link"][contains(., "Настройки")]'},
            'Клик_переход_в_настройки': {'func': page.click_xpath, 'path': './/a[@class="tabs__link js-tabs-link"][contains(., "Настройки")]'},
            'Клик_день_рождения': {'func': page.click_id, 'path': 'birthday-day'},
            'Ввод_дня_рождения': {'func': page.click_css, 'path': '#birthday-day > option:nth-child(5)'},
            'Клик_месяц_рождения': {'func': page.click_id, 'path': 'birthday-month'},
            'Ввод_месяца_рождения': {'func': page.click_css, 'path': '#birthday-month > option:nth-child(5)'},
            'Клик_год_рождения': {'func': page.click_id, 'path': 'birthday-year'},
            'Ввод_года_рождения': {'func': page.click_xpath, 'path': './/option[@value="1990"]'},
            'Клик_выбран_пол': {'func': page.click_xpath, 'path': './/span[@class="toggle__label"][contains(., "Мужской пол")]'},
            
            'Клик_Снятие_галочки_с_подписки': {'func': page.click_xpath, 'path': './/span[text()="Да, я хочу получать подписку с обновлениями, акциями и подарками"]'},
            'Клик_Снятие_галочки_с_продолжения_просмотра': {'func': page.click_xpath, 'path': './/span[text()="Продолжать просмотр с места остановки"]'},
            'Клик_Сохранить': {'func': page.click_xpath, 'path': './/button[@class="cabinet-settings__button button button_stretched"][contains(., "Сохранить")]'},
            'Клик_Избранное': {'func': page.click_xpath, 'path': './/a[text()="Избранное"]'},

        }
        # Profile
        self.args = self.profx[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')

class MainPage(BasePage):
    def click_f(self, name, stap):
        step = str(stap)
        self.pagex = {
            'Клик_прокрутки_слайда_вправо':{'func': self.click_xpath, 'path': './/button[@class="slider__navigation slider__navigation_next js-slider-navigation js-slider-navigation-next"]'},
            'Клик_прокрутки_слайда_влево': {'func': self.click_xpath,'path': './/button[@class="slider__navigation slider__navigation_prev js-slider-navigation js-slider-navigation-prev"]'},
            'Клик_поиска_Лупа': {'func': self.click_css,'path': '#header-search-button'},
            'Клик_кнопки_крестик': {'func': self.click_xpath,'path': './/button[@class="modal__close"]'},
            'Клик_Новинки': {'func': self.click_xpath,'path': './/a[@href="/novinki/"]'},  
            'Показать_еще': {'func': self.click_xpath,'path': './/button[@class="catalog__more button js-catalog-more"]'},
            #Подписки
            'Клик_Подписки': {'func': self.click_xpath,'path': './/a[@title="Подписка tvzavr"]'},
            'Клик_Подписка_Отключи_рекламу': {'func': self.click_xpath,'path': './/a[@class="tabs__link js-tabs-link"][contains(., "«Отключи рекламу на tvzavr!»")]'},
            'Клик_купить_за_99р': {'func': self.click_xpath, 'path': './/button[@class="subscriptions__button button button_dark js-payment-info"]'},
            'Клик_Бесплатно': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Бесплатно")]'},
            #Каталог и разделы 
            'Клик_Каталог': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Каталог")]'}, 
            'Клик_Фильмы_в_каталоге': {'func': self.click_xpath, 'path': './/button[@class="filter__category js-filter-category"][contains(., "Фильмы")]'},
            'Клик_Мультфильмы_в_каталоге': {'func': self.click_xpath, 'path': './/button[@class="filter__category js-filter-category"][contains(., "Мультфильмы")]'},
            'Клик_Сериалы_в_каталоге': {'func': self.click_xpath, 'path': './/button[@class="filter__category js-filter-category"][contains(., "Сериалы")]'},
            'Клик_Годы_выпуска': {'func': self.click_xpath, 'path': './/button[@class="filter__subcategory js-filter-subcategory"][contains(., "Годы выпуска")]'},
            'Выставление_год_левый': {'func': self.click_xpath, 'path': './/div[@style="left: 22.7642%;"]'},
            'Клик_Родительский_контроль': {'func': self.click_xpath, 'path': './/span[text()="Родительский контроль"]'},
            'Клик_Бесплатные': {'func': self.click_xpath, 'path': './/span[text()="Бесплатные"]'},
            
            # Страны
            'Клик_страны': {'func': self.click_xpath, 'path': './/button[@class="filter__subcategory js-filter-subcategory"][contains(., "Страны")]'},
            'Клик_США': {'func': self.click_xpath,'path': './/li[@data-filter-id="515"]'},
            'Клик_Германия': {'func': self.click_xpath,'path': './/li[@data-tag-name="Германия"]'},
            'Клик_Южная_Корея': {'func': self.click_xpath,'path': './/li[@data-filter-id="8789"]'},
            'Клик_Япония': {'func': self.click_xpath,'path': './/li[@data-filter-id="3467"]'},
            'Клик_Испания': {'func': self.click_xpath,'path': './/li[@data-filter-id="2600"]'},
            'Клик_Турция': {'func': self.click_xpath,'path': './/li[@data-filter-id="5287"]'},
            'Клик_Россия': {'func': self.click_xpath,'path': './/li[@data-filter-id="122"]'},
            # Жанры
            'Клик_Жанры': {'func': self.click_xpath, 'path': './/button[@class="filter__subcategory js-filter-subcategory"][contains(., "Жанры")]'},
            'Клик_боевик_жанр': {'func': self.click_xpath,'path': './/li[@data-filter-id="690"]'},
            'Клик_комедия_жанр': {'func': self.click_xpath,'path': './/li[@data-tag-name="Комедия"]'},
            'Клик_азиатский_жанр': {'func': self.click_xpath,'path': './/li[@data-filter-id="21136"]'},
            'Клик_Советский_жанр': {'func': self.click_xpath,'path': './/li[@data-filter-id="7320"]'},
            'Клик_приключения_жанр': {'func': self.click_xpath,'path': './/li[@data-filter-id="702"]'},
            'Клик_Детектив_жанр': {'func': self.click_xpath,'path': './/li[@data-filter-id="693"]'},
            'Клик_применить_фильтр': {'func': self.click_xpath, 'path': './/button[@class="filter__apply button js-filter-apply"]'},

            'Клик_кнопки_просмотр_от_руб': {'func': self.click_xpath, 'path': './/button[@class="clip-player__action button"]'},
            'Клик_Сериалы': {'func': self.click_xpath,'path': './/a[text()="Сериалы"]'},
            'Клик_Вход': {'func': self.click_xpath,'path': './/button[@class="header__login"]'},
            # Mail
            'Клик_Вход_через_Mailru': {'func': self.click_xpath,'path': './/a[@class="social__link social__link_mr js-social-link"]'},
            'Клик_Войти_и_разрешить_Mailru': {'func': self.click_xpath,'path': './/button[@class="ui-button-main"][contains(., "Войти и разрешить")]'},
            # FaceBook
            'Клик_Вход_через_FB': {'func': self.click_xpath,'path': './/a[@class="social__link social__link_fb js-social-link"]'},  # login-social__link login-social__link_fb js-login-social-link
            'Клик_Вход_через_VK': {'func': self.click_xpath,'path': './/a[@class="social__link social__link_vk js-social-link"]'},
            'Клик_Вход_через_OK': {'func': self.click_xpath,'path': './/a[@class="social__link social__link_ok js-social-link"]'},
            'Клик_Вход_через_G': {'func': self.click_xpath,'path': './/a[@class="social__link social__link_gp js-social-link"]'},
            
            'Клик_Вход_FB': {'func': self.click_id,'path': 'loginbutton'},
            'Клик_Вход_VK': {'func': self.click_id,'path': 'install_allow'},
            'Клик_Вход_ОК': {'func': self.click_xpath,'path': './/input[@class="button-pro __wide form-actions_yes"]'},
            'Снятие_галочки_чекбокса_запомнить_меня': {'func': self.click_xpath,'path': './/span[@class="irc-vis"]'},
            'Клик_кнопки_Далее_Google': {'func': self.click_xpath,'path': './/span[@class="RveJvd snByac"][contains(., "Далее")]'},
            'Клик_1_Далее_Google': {'func': self.click_xpath,'path': './/span[@class="RveJvd snByac"][contains(., "Далее")]'},
            'Клик_Войти_auth': {'func': self.click_id,'path': 'authorization-submit'},
            'По_номеру_телефона': {'func': self.click_xpath,'path': './/a[@data-target="register-phone-tab"]'},
            #Подборки
            'Клик_Подборки': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Подборки")]'},
            'Клик_Коллекции': {'func': self.click_xpath,'path': './/a[@class="filter__category"][contains(., "Коллекции")]'},
            'Клик_Подборки_партнеров': {'func': self.click_xpath,'path': './/a[@class="filter__category"][contains(., "Подборки партнеров")]'},

            'Клик_Детям': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Детям")]'},

            'Клик_Спецпроекты': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Спецпроекты")]'},
            'Клик_Кино_равного_доступа': {'func': self.click_xpath,'path': './/div[@class="card__title"][contains(., "Кино равного доступа")]'},
            'Проект, где ваши дети снимаются в кино': {'func': self.click_xpath,'path': './/div[@class="card__title"][contains(., "Проект, где ваши дети снимаются в кино")]'},
            'Клик_TVZ': {'func': self.click_xpath,'path': './/div[@class="card__title"][contains(., "Кино равного доступа")]'},   #

            'Обратная_связь': {'func': self.click_xpath,'path': './/button[@class="footer__link"][contains(., "Обратная связь")]'},
            'Клик_Отправить_сообщение': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Подборки")]'},
            'Клик_Отправить_сообщение_обратная связь': {'func': self.click_xpath,'path': './/button[@class="feedback__submit button button_stretched"]'},
            'Редактировать': {'func': self.click_xpath,'path': './/a[@class="header__link"][contains(., "Редактировать")]'},
            'Клик_первого_фильма': {'func': self.click_xpath,'path': './/div[@class="owl-item active"]'},
            'Клик_постер_первого_фильма': {'func': self.click_xpath,'path': './/a[@class="card card_clip"]'},
            'Клик_постер_сериала_соседка_ты_дома': {'func': self.click_xpath,'path': '//a[@href="/film/sosedka-ty-doma/"]'},
            'Клик_стрелка_Вниз': {'func': self.click_tag,'path': 'body', 'send':Keys.DOWN},
            'Переход_вниз_страницы': {'func': self.click_tag,'path': 'body', 'send':Keys.END},
        }
              #   MainPage
        self.args = self.pagex[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')

    def send_f(self, name, text, stap):
        step = str(stap)
        self.pages = {
            'Ввод_в_строку_поиска': {'func': self.send_id, 'path': 'search-field', 'text':text},
            'Ввод_2_в_строку_поиска': {'func': self.send_id, 'path': 'header-search-field', 'text':text},
            # Регистрация ТВЗАВР
            #'Ввод_логина': {'func': self.send_name, 'path': 'email', 'text':text},
            'Ввод_логина': {'func': self.send_name, 'path': 'email-registration__address', 'text':text},
            'Ввод_пароля': {'func': self.send_css, 'path': '#register-email-password', 'text':text},
            # Вход ТВЗАВР
            'Ввод_логина_вход': {'func': self.send_name, 'path': 'login', 'text':text},
            'Ввод_пароля_вход': {'func': self.send_css, 'path': '#auth-password', 'text':text},
            # Гугл
            'Ввод_логин_Google': {'func': self.send_id, 'path': 'identifierId', 'text':text},
            'Ввод_пароль_Google': {'func': self.send_name, 'path': 'password', 'text':text},
            # Mail
            'Ввод_логин_Mailru': {'func': self.send_name, 'path': 'Login', 'text':text},
            'Ввод_пароля_Mailru': {'func': self.send_css, 'path': '#password', 'text':text},
            # Facebook
            'Ввод_пароля_FB': {'func': self.send_css, 'path': '#pass', 'text':text},
            # VK
            'Ввод_пароля_VK': {'func': self.send_css, 'path': '#login_submit > div > div > input:nth-child(9)', 'text':text},
            # Одноклассники
            'Ввод_логина_OK': {'func': self.send_name, 'path': 'fr.email', 'text':text},
            'Ввод_пароля_OK': {'func': self.send_css, 'path': '#field_password', 'text':text},

            'Ввод_сообщения_скайп': {'func': self.send_id, 'path': '#.public-DraftStyleDefault-block', 'text':text},
            
            'Ввод_name_логина': {'func': self.send_name, 'path': 'login', 'text':text},
            'Ввод_номера_телефона_reg': {'func': self.send_name, 'path': 'phone', 'text':text},
            'Ввод_СМС_пароля_reg': {'func': self.send_name, 'path': 'code', 'text':text},
            'feedback_имя_пользователя': {'func': self.send_id, 'path': 'feedback-name', 'text':text},
            'feedback_e_mail_пользователя': {'func': self.send_id, 'path': 'feedback-email', 'text':text},
            'feedback_сообщение_пользователя': {'func': self.send_id, 'path': 'feedback-decription', 'text':text},
            'Ввод_ответа_пользователю': {'func': self.send_id, 'path': 'issue_notes', 'text':text},
            'Ввод_текста_ответа_пользователя': {'func': self.send_id, 'path': 'tinymce', 'text':text},
            # Админка
            #'Ввод_имени_в_Redmine': {'func': self.send_id, 'path': 'username', },          
            'Ввод_номера_телефона_auth': {'func': self.send_css, 'path': '#auth-login', 'text':text},
            'Ввод_из_СМС_пароля_auth': {'func': self.send_css, 'path': '#auth-password', 'text':text},
            #'Ввод_сообщения_в_skype': {'func': self.send_css, 'path': '.public-DraftStyleDefault-block', 'text':text},
            'Ввод_суммы_пополнения_счета': {'func': self.send_name, 'path': 'price', 'text':text},
            'Ввод_профиль_old_пароля': {'func': self.send_id, 'path': 'cabinet-password-old', 'text': text},
            'Ввод_профиль_new_пароля': {'func': self.send_id, 'path': 'cabinet-password-new', 'text': text},
            'Ввод_профиль_rep_пароля': {'func': self.send_id, 'path': 'cabinet-password-repeat', 'text': text},
            'Ввод_псевдонима': {'func': self.send_id, 'path': 'name', 'text': text},
            'Админка_Ввод_в_поиск': {'func': self.send_name, 'path': 'q_q', 'text': text},
            'Ввод_номера_карты_тройка': {'func': self.send_id, 'path': 'troika-binding-textbox', 'text': text},
            # Оплата картой
            #'Ввод_номер_карты': {'func': self.send_name, 'path': }
        }
        self.args = self.pages[name]
        self.func = self.args['func']  # имя функции из словаря
        self.func(self.args)  # Вызов нужной функции с id = path
        self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')

    #  Функция клик пропуска фулл скрина test case 9 + all Sony
    def click_button(self, bc):
        button_xpath = ('.//button[text()="%s"]' % bc)
        # self.loger_info(button_xpath)
        self.driver.find_element_by_xpath(button_xpath).click()

    #  Функция клик кнопок верхнего меню
    def click_div(self, dep):
        up_xpath = ('.//div[text()="%s"]' % dep)
        self.waitForElementClickable(up_xpath, 30)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath(up_xpath).click()
        # print('Клик', dep)
        return

    #  Функция клик вкладок
    def click_li(self, dep):
        li_xpath = ('.//li[text()="%s"]' % dep)
        self.waitForElementClickable(li_xpath, 30)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath(li_xpath).click()
        # print('Клик', dep)

    #  Функция клик вкладок .//a[text()="%s"]
    def click_a(self, dep):
        a_xpath = ('.//a[text()="%s"]' % dep)
        self.waitForElementClickable(a_xpath, 10)
        self.driver.find_element_by_xpath(a_xpath).click()
        # print('Клик', dep)

    #  Функция клик вкладок
    def click_span(self, dep):
        span_xpath = ('.//span[text()="%s"]' % dep)
        self.waitForElementClickable(span_xpath, 30)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath(span_xpath).click()
        # print('Клик', dep)

    def click_id(self, args):
        dep = args['path'] 
        self.waitForIDVisible(dep, 10) 
        self.driver.find_element_by_id(dep).click()
        # print('Клик', dep)

    def click_name(self, args):
        dep = args['path']
        self.waitForNameVisible(dep, 30)
        self.driver.find_element_by_name(dep).click()
        # print('Клик', dep)

    def click_xpath(self, args):
        xpath = args['path']
        self.waitForElementClickable(xpath, 30)
        self.driver.find_element_by_xpath(xpath).click()

    def click_css(self, args):
        css = args['path']
        print('css = ', css)
        # self.waitForElementClickable(css, 30)
        self.driver.find_element_by_css_selector(css).click()

    def click_switch_to(self, args):
        frame = args['path']
        index = args['index']
        # self.waitForElementClickable(css, 30)
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name(frame)[index]).click()

    def click_s_xpath(self, args):
        xpath = args['path']
        index = args['index']
        self.waitForElementClickable(xpath, 30)
        self.driver.find_elements_by_xpath(xpath)[index].click()

    def double(self, args):
        self.click_xpath(args['path_1'])
        self.click_xpath(args['path_2'])

    def click_tag(self, args):
        self.driver.find_element_by_tag_name(args['path']).send_keys(args['send'])

    # Проверка видимости элемента                                         #Exception
    def tester_vis_xpath(self, xpath):
        self.waitForElementVisible(xpath, 5)
        self.driver.find_element_by_xpath(xpath)
        # print('Клик', dep)

    # Проверка кликабельности элемента
    def tester_click_xpath(self, xpath):
        self.waitForElementClickable(xpath, 25)
        self.driver.find_element_by_xpath(xpath)
        # print('Клик', dep)

    # Кнопки
    def click_play(self):
        xpath = '//*[@id="clip-player"]/div[16]'
        self.waitForElementClickable(xpath, 35)
        self.driver.find_element_by_xpath(xpath).click()
        # # print('Клик', dep)

    def click_stop(self):
        # xpath = '//*[@id="clip-player"]/div[4]'
        xpath = '//*[@id="clip-player"]/div[4]/div'
        # xpath = '//*[@id="clip-player"]/div[3]'
        css_sel = '#clip-player > div.tvz-button.tvz-button_play > div'
        # self.waitForElementClickable(xpath, 15)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath(xpath).click()
        # self.driver.find_element_by_css_selector(css_sel).click()
        # print('Клик', dep)

    def click_enter(self):
        self.click_xpath('.//button[@class="header__login"]')

    def waitForElementPresent(self, xpath, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def waitForElementClickable(self, xpath, timer):
        WebDriverWait(self.driver, timer).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def waitForElementVisible(self, xpath, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def waitForNameVisible(self, name, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.NAME, name)))

    def waitForIDVisible(self, id, timer):
        WebDriverWait(self.driver, timer).until(EC.presence_of_element_located((By.ID, id)))

    #                                                OPERATIONS

    # Функция ввода
    def send_id(self, args):
        d_id = args['path']
        txt = args['text']
        # self.loger_info('path = ' + d_id + ', text = ' + txt)
        self.waitForIDVisible(d_id, 30)
        self.driver.find_element_by_id(d_id).send_keys(txt)
        return

    def send_name(self, args):
        d_name = args['path']
        txt = args['text']
        self.waitForNameVisible(d_name, 30)
        self.driver.find_element_by_name(d_name).send_keys(txt)
        return

    def send_css(self, args):
        d_name = args['path']
        txt = args['text']
        self.driver.find_element_by_css_selector(d_name).send_keys(txt)
        return

    # Функция ввода
    def input(self, dclass, data):
        li_xpath = ('.//input[@class="%s"]' % dclass)
        # self.waitForElementClickable(li_xpath, 80)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath(li_xpath).send_keys(data)

    def rand_mail(self, lit):
        d = str(datetime.today())
        ds = d.replace('-', '')
        d = ds.split(':')[0]
        d_2 = ds.split(':')[1]
        d_3 = d.replace(' ', '')
        rand = d_3 + d_2
        # self.loger_info(rand)
        random_mail = 'tvzavrtest' + rand + lit + '@rrbbxvdr.rz'
        return (random_mail, rand)

    # def rand_number(self, lit):
    #     d = str(datetime.today())
    #     ds = d.replace('-', '')
    #     d = ds.split(':')[0]
    #     d_2 = ds.split(':')[1]
    #     d_3 = d.replace(' ', '')
    #     rand = d_3 + d_2
    #     self.loger_info(rand)
    #     random_number = rand + lit
    #     return (random_number, rand)
        
    def code_phone(self, phone):
        self.loger_info('Получение кода на телефон:  ' + phone)
        #url = 'http://www.tvzavr.ru/api/3.1/sms/send_confirm_code?phone=' + str(phone) + '&entity=empty&prv=smsfake_tvz'
        url = 'http://www.tvzavr.ru/api/3.1/sms/send_confirm_code?phone=' + str(phone) + '&entity=empty&prv=smstest_tvz'  #получилось с этой
        self.loger_info(url)
        code = (requests.get(url)).text
        self.loger_info('code_phone ' + code)
        r_code = code.split(':')[3]
        s_code = r_code.split('"')[1]
        self.loger_info(s_code)
        return s_code

    # Функция проверки наличия элементов на странице.
    def elem(self):
        self.loger('Проверка элементов страницы')
        # Проверка наличия ссылки "Новинки""
        res_txt = str(ResultPage.find_link(self, "a", "header__link"))
        self.loger(res_txt)
        # Новинки - проверочное словосочетание надписи
        assert ('Новинки') in res_txt
        self.loger('Наличие ссылки "Новинки" подтверждено')
        # Проверка наличия ссылки "Подписки""
        res_txt = str(ResultPage.find_all_link(self, "a", "header__link"))
        # Подписки - проверочное словосочетание надписи
        assert ('Подписки') in res_txt
        self.loger('Наличие ссылки "Подписки" подтверждено')
        # Проверка наличия ссылки "Бесплатно""
        # Бесплатно - проверочное словосочетание надписи
        assert ('Бесплатно') in res_txt
        self.loger('Наличие ссылки "Бесплатно" подтверждено')
        # Проверка наличия ссылки "Подборки"
        # Подборки - проверочное словосочетание надписи
        assert ('Подборки') in res_txt
        self.loger('Наличие ссылки "Подборки" подтверждено')
        # Проверка наличия ссылки "Каталог""
        # Каталог - проверочное словосочетание надписи
        assert ('Каталог') in res_txt
        self.loger('Наличие ссылки "Каталог" подтверждено')
        # Проверка наличия ссылки "Детям""
        # Детям - проверочное словосочетание надписи
        assert ('Детям') in res_txt
        self.loger('Наличие ссылки "Детям" подтверждено')
        # Проверка наличия ссылки "Вход""
        res_txt = str(ResultPage.find_link(self, "button", "header__login"))
        # Вход - проверочное словосочетание надписи
        assert ('Вход') in res_txt
        self.loger(res_txt)
        self.loger('Наличие ссылки "Вход" подтверждено')

    def loger(self, text):
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG)
        logging.info(text)
        print(text)

    def loger_info(self, text):
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG)
        logging.info(text)
        print(text)

    def loger_error(self, text):
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG)
        logging.error(text)
        print(text)

    def send_sms(self, phone, message):  # Функция отправки смс
        logging.info("Вызов функции отправки СМС")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")  # Запуск браузера с сохраненным профилем
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://app.mysms.com/")
        self.driver.implicitly_wait(10)
        time.sleep(SLEEP_MEDIUM)
        self.driver.find_element_by_xpath('.//div[@class="gwt-Label"]').click()  # Новое сообщение
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath('.//input[@class="recipientTextBox"]').send_keys(phone)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath('.//div[@class="textarea"]').send_keys(message)
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath('.//button[@class="styledButton sendButton sim dropdown"]').click()
        logging.info("Клик 'Отправить' произведен, СМС подтверждения отправлено")
        self.driver.close()
        return

    def login_google(self, emailgo, passok):
        time.sleep(SLEEP_SHORT)
        self.send_f('Ввод_логин_Google', emailgo, 1)
        time.sleep(2)
        self.click_f('Клик_кнопки_Далее_Google', 6)
        time.sleep(2)
        self.send_f('Ввод_пароль_Google', passok, 1)
        time.sleep(2)
        self.click_f('Клик_кнопки_Далее_Google', 6)
        time.sleep(2)
        return

    # def login_tvzavr(self, emailt, passw):
    #     time.sleep(SLEEP_SHORT)
    #     self.send_f('Ввод_name_логина', emailt, 2)
    #     self.send_f('Ввод_пароля_tvz', passw, 3)
    #     self.click_f('Клик_Войти_auth', 4)
    #     time.sleep(SLEEP_MEDIUM)
    #     return 06.08.2019

    def login_tvzavr(self, emailt, passw):
        self.click_f('Клик_Вход', 1)
        time.sleep(SLEEP_SHORT)
        self.send_f('Ввод_name_логина', emailt, 2)
        self.send_f('Ввод_из_СМС_пароля_auth', passw, 3)
        self.click_f('Клик_Войти_auth', 4)
        time.sleep(SLEEP_MEDIUM)
        return


    # def login_tvzavr(self, email, passw, sex): 1.08.2019
    #     result = ResultPage(self.driver)
    #     prof = Profile(self.driver)
    #     self.waitForElementVisible('.//button[@class="header__login"]', 7)
    #     resic = result.find_link("button", "header__login")
    #     if "Вход" not in resic:
    #         if sex == 'male':
    #             prof.click_f('Клик_Аватарка_М', 1)
    #         else:
    #             prof.click_f('Клик_Аватарка_Ж', 1)

    #         prof.click_f('Клик_Выйти', 1)

    #     else:
    #         # Шаг 1 Нажать в шапке на кнопку "Вход".')
    #         self.click_f('Клик_Вход', 1)
    #         time.sleep(SLEEP_SHORT)
    #         # Шаг 2
    #         self.send_f('Ввод_name_логина', email, 2)
    #         self.send_f('Ввод_пароля_Google', passw, 3)
    #         self.click_f('Клик_Войти_auth', 4)

            # time.sleep(SLEEP_LONG)
            # try:
            #     self.click_f('Клик_кнопки_крестик', 6)
            # except:
            #     print('нет акции мицубиси')
            # Шаг 5
        #     if sex == 'male': 1.08.2019
        #         prof.click_f('Клик_Аватарка_М', 7)
        #     else:
        #         prof.click_f('Клик_Аватарка_Ж', 8)
        #     time.sleep(SLEEP_MEDIUM)
        # return

    def login_mailru(self, emailru, passw):
        self.send_id('mailbox:login', emailru)
        self.loger_info('Ввод логина на mail.ru ' + emailru + 'произведен')
        time.sleep(SLEEP_SHORT)
        self.send_id('mailbox:password', passw)
        self.loger_info('Ввод пароля на mail.ru произведен')
        time.sleep(SLEEP_SHORT)
        self.driver.find_element_by_xpath('.//input[@class="o-control"]').click()
        self.loger_info('Клик кнопки "Войти" на mail.ru произведен')
        time.sleep(SLEEP_MEDIUM)

    def registration(self, email, passw):
        result = ResultPage(self.driver)
        prof = Profile(self.driver)
        resic = result.find_link("button", "header__login tvz-unauthorized")
        if "Вход" not in resic:
            prof.click_f('Клик_Аватарка_М', 1)
            self.loger_info('Шаг 0 Клик на аватарку пользователя произведен')
            self.driver.find_element_by_xpath('.//button[@class="profile-menu__logout js-profile-logout"]').click()
            time.sleep(SLEEP_SHORT)
        else:
            self.click_enter()
            self.loger_info('Шаг 1 Клик "Вход" произведен')
            # Шаг 2
            self.click_a('Регистрация')
            self.loger_info('Шаг 2 Клик "Регистрация" произведен')
            time.sleep(SLEEP_SHORT)
            # Шаг 3
            self.login('email', email)
            print('Шаг 3 Ввод логина', email, 'произведен')
            # Шаг 4
            self.driver.find_element_by_css_selector('#register-email-password').send_keys(passw)
            # page.login('password', passw)
            self.loger_info('Шаг 4 Ввод пароля произведен')
            time.sleep(SLEEP_SHORT)
            # Шаг 5
            self.driver.find_element_by_id('register-email-submit').click()
            self.loger_info('Шаг 5 Клик "Зарегистрироваться" произведен')
            time.sleep(7)
            prof.click_f('Клик_Аватарка_М', 5)

            self.loger_info('Шаг 6 Клик на аватарку пользователя произведен')
            self.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 7)
            # Проверка авторизации пользователя"
            resic = str(result.find_link("div", "profile-menu__name __username"))
            # email - проверочное словосочетание надписи
            assert (email) in resic
            self.loger_info('Авторизация зарегистрированного пользователя с е-майлом ' + email + ' подтверждена')

            time.sleep(SLEEP_SHORT)

    def input_card(self, number, month, year, name_card, cvv):
        result = ResultPage(self.driver)
        self.driver.find_elements_by_xpath('.//input[@class="payment-cloudpayments__field textbox js-input"]')[0].send_keys(number)
        self.loger_info('Шаг 10 Ввод номера карты произведен ' + number)
        time.sleep(3)
        self.driver.find_elements_by_xpath('.//select[@class="dropdown js-input"]')[0].click()
        time.sleep(1)
        self.driver.find_element_by_xpath('.//option[@value="%s"]' % month).click()
        self.loger_info('Ввод месяца карты произведен')
        time.sleep(3)
        self.driver.find_elements_by_xpath('.//select[@class="dropdown js-input"]')[1].click()
        self.driver.find_element_by_xpath('.//option[@value="%s"]' % year).click()
        self.loger_info('Ввод года карты произведен')
        time.sleep(3)
        # Заполнить поле "Имя держателя" - Ivanov Ivan
        self.driver.find_elements_by_xpath('.//input[@class="payment-cloudpayments__field textbox js-input"]')[1].send_keys(name_card)
        self.loger_info('Ввод имени держателя карты произведен')
        time.sleep(3)
        # Заполнить поле "CVV код" - 526
        self.driver.find_element_by_xpath('.//input[@class="payment-cloudpayments__field payment-cloudpayments__field_cvc textbox js-input"]').send_keys(cvv)
        self.loger_info('Ввод CVV код карты произведен')
        time.sleep(4)
        # Снять галочку "Сохранить данные карты"

        # self.driver.find_element_by_xpath('.//span[@class="toggle__label"]').click()
        # self.loger_info('Снятие галочки в чек-боксе"Сохранить данные карты" произведено')

        #  Нажать кнопку "Оплатить"clip-watch
        self.driver.find_element_by_xpath('.//button[@class="payment-cloudpayments__pay button button_stretched js-buy-button"]').click()
        self.loger_info('Клик "Оплатить" произведен')
        time.sleep(1)
        # message = str(result.find_link("section", "tvz-alerts tvz-animation-fadeOut"))
        # self.loger_info('Сообщение внизу формы оплаты:')
        # self.loger_info('message:' + message)
        

    def delete_mails(self, emailgo, passgo):
        # self.driver.get('https://mail.google.com')
        self.loger_info('Шаг 5 Переход на gmail.com произведен')
        # self.login_google(emailgo, passgo)
        time.sleep(SLEEP_SHORT)
        # self.driver.get('https://mail.google.com/mail/u/0/#inbox')
        # Удаление письма из почты
        self.click_xpath('.//div[@class="J-J5-Ji J-JN-M-I-Jm"]')
        # self.driver.find_element_by_id(':3d').click()
        self.loger_info('Поставлена галочка чекбокс - выбор письма')
        self.click_xpath('//*[@id=":5"]/div/div[1]/div[1]/div/div/div[2]/div[3]')
        # self.click_xpath('.//div[@class="T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA"]')
        self.loger_info('Клик кнопки "Удалить" письмо на gmail.com произведен')
        time.sleep(SLEEP_SHORT)

    def consol_jenkins(self):
        print('Запуск проверки консоли')
        # p = subprocess.call('ffmpeg.exe -framerate 10 -f image2 -i "Frame%03d.jpg" -r 10 -s 620x380 Video.avi', shell=True)
        options = webdriver.ChromeOptions()
        # options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://192.168.2.31:8080/jenkins/job/1_Regress/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        page = MainPage(self.driver)
        result = ResultPage(self.driver)
        self.send_name('j_username', 'admin')
        self.send_name('j_password', 'admin')
        self.click_xpath('.//div[@class="Checkbox-indicator"]')
        self.click_name('Submit')
        self.driver.implicitly_wait(5)
        self.driver.find_elements_by_xpath('.//td[@class="build-row-cell"]')[0].click()
        self.click_a('Вывод консоли')
        res = self.driver.find_element_by_xpath('.//pre[@class="console-output"]').text
        self.driver.close()
        return res

    def mail_send_web(self, login, passw):
        self.driver.execute_script("window.open('','_blank');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        result = ResultPage(self.driver)
        self.driver.get("https://e.mail.ru/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.loger_info(' Переход в mail произведен')
        time.sleep(2)


        #self.driver.find_element_by_name("Login").send_keys('testmailtvzavr15')
        self.driver.find_element_by_xpath('.//*[@id="root"]/div/div[3]/div/div/div/form/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]')[0].click()
        self.driver.find_element_by_xpath('.//*[@id="root"]/div/div[3]/div/div/div/form/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]').send_keys('testmailtvzavr15')
        time.sleep(2)

        self.driver.find_element_by_xpath('.//span[@class="c01104 c0179 c01102 c0177"]').click() # Клик далее
        time.sleep(3)






    def scype_send_web(self, login, passw):
        self.driver.execute_script("window.open('','_blank');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        result = ResultPage(self.driver)
        # options = webdriver.ChromeOptions()
        # options.add_argument("--disable-notifications")
        # options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        # self.driver = webdriver.Chrome(options=options)
        
        self.driver.get("https://web.skype.com/ru/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.loger_info(' Переход в Skype произведен')
        time.sleep(2)

        self.driver.find_element_by_name("loginfmt").send_keys('79776410337')
        time.sleep(2)
        
        self.driver.find_element_by_xpath('.//input[@id="idSIButton9"]').click() # Клик далее
        time.sleep(3)

        self.driver.find_element_by_name("passwd").send_keys('Aleh1260337')
        self.loger_info('Ввод Skype пароля произведен')
        time.sleep(3)

        self.driver.find_element_by_xpath('.//input[@id="idSIButton9"]').click() # Клик вход
        self.loger_info('Клик Вход произведен')
        time.sleep(3)

        self.driver.find_element_by_xpath('.//div[@id="rx-vlv-6"]').click() # Клик по диалогу
        self.loger_info('Шаг 100.   Переход в чат Деплоймент произведен')
        time.sleep(10)

        
        self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block").click() # Клик по полю ввода
        time.sleep(15)
        
        print('тут2222')
        time.sleep(2)


        #self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[3]').send_keys('text')
        #self.send_f('Ввод_сообщения_скайп', 'text', 15)
        #self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[2]').send_keys('text')
        self.driver.find_element_by_css_selector('[id="#.public-DraftStyleDefault-block"]').send_keys('text')
        


        self.page.loger('тут')
        self.click_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/label/div/div/div[2]/div[2]/div/swx-button/button')
        self.loger_info('Отправка текста в чат Деплоймент произведена')
        self.driver.close()





    def delete_uzer(self, name):     # ФУНКЦИЯ УДАЛЕНИЯ ПОЛЬЗОВАТЕЛЯ ИЗ АДМИНКИ
        self.driver.execute_script("window.open('','_blank');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.get("https://www.tvzavr.ru:8080/admin/")
        time.sleep(2)
        # 'Открытие страницы админки
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_xpath('.//a[@href="https://accounts.google.com/o/oauth2/auth?client_id=245544346256-4luf263ioa376hp89q5k08otplt9dvdh.apps.googleusercontent.com&scope=openid%20profile%20email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fplus.login&redirect_uri=http://www.tvzavr.ru:8080/oauth2callback/&response_type=code"]').click()
        time.sleep(3)
        # Логинимся через Google
        
        emailgo = 'bykov.a@tvzavr.ru'
        passok = 'tmW9HZvaksgc'

        self.send_f('Ввод_логин_Google', emailgo, 1)
        time.sleep(2)
        self.click_f('Клик_кнопки_Далее_Google', 6)
        time.sleep(2)
        self.send_f('Ввод_пароль_Google', passok, 1)
        time.sleep(2)
        self.click_f('Клик_кнопки_Далее_Google', 6)
        time.sleep(6)
        # Вошли в админку
                
        self.driver.find_element_by_xpath('.//a[@href="/admin/tvzavr_admin/customer/"]').click() # Клик на "Профили посетителей"
        time.sleep(3)
        self.send_f('Админка_Ввод_в_поиск', name, 16) # Ввод имени пользователя
        time.sleep(3)
        
        self.driver.find_element_by_xpath('.//input[@value="Найти"]').click()  # Клик найти
        time.sleep(2)
        
        self.driver.find_element_by_xpath('.//input[@id="action-toggle"]').click() # Клик по чекбоксу(ставит галочку)   
        time.sleep(2)

        self.driver.find_element_by_xpath('.//select[@name="action"]').click()  # Клик на поле "Действие"
        time.sleep(2)
        self.driver.find_element_by_css_selector('#action_block > label > select > option:nth-child(14)').click() # Выбор "Удалить"
        time.sleep(2)
        self.driver.find_element_by_xpath('.//*[@id="action_block"]/button').click() # Клик на "Выполнить"
        time.sleep(3)
        self.driver.find_element_by_xpath('.//*[@id="content"]/form/div[2]/input[4]').click() # Клик на "Да, уверен"
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)



    def delete_comments(self, name):     # ФУНКЦИЯ УДАЛЕНИЯ комментариев ПОЛЬЗОВАТЕЛЯ
        self.driver.execute_script("window.open('','_blank');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.driver.get("https://www.tvzavr.ru:8080/admin/")
        time.sleep(2)
        # 'Открытие страницы админки
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.implicitly_wait(7)
        self.driver.find_element_by_xpath('.//a[@href="https://accounts.google.com/o/oauth2/auth?client_id=245544346256-4luf263ioa376hp89q5k08otplt9dvdh.apps.googleusercontent.com&scope=openid%20profile%20email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fplus.login&redirect_uri=http://www.tvzavr.ru:8080/oauth2callback/&response_type=code"]').click()
        time.sleep(3)
        # Логинимся через Google
        
        emailgo = 'bykov.a@tvzavr.ru'
        passok = 'tmW9HZvaksgc'

        self.send_f('Ввод_логин_Google', emailgo, 1)
        time.sleep(2)
        self.click_f('Клик_кнопки_Далее_Google', 6)
        time.sleep(2)
        self.send_f('Ввод_пароль_Google', passok, 1)
        time.sleep(2)
        self.click_f('Клик_кнопки_Далее_Google', 6)
        time.sleep(6)
        # Вошли в админку
                
        self.driver.find_element_by_xpath('.//a[@href="/admin/tvzavr_admin/customer/"]').click() # Клик на "Профили посетителей"
        time.sleep(3)
        self.send_f('Админка_Ввод_в_поиск', name, 16) # Ввод имени пользователя
        time.sleep(3)
        
        self.driver.find_element_by_xpath('.//input[@value="Найти"]').click()  # Клик найти
        time.sleep(2)
        
        self.driver.find_element_by_xpath('.//input[@id="action-toggle"]').click() # Клик по чекбоксу(ставит галочку)   
        time.sleep(2)

        self.driver.find_element_by_xpath('.//select[@name="action"]').click()  # Клик на поле "Действие"
        time.sleep(2)
        self.driver.find_element_by_xpath('.//option[@value="remove_comments"]').click()
        #self.driver.find_element_by_css_selector('#action_block > label > select > option:nth-child(14)').click() # Выбор "Удалить"
        time.sleep(2)
        self.driver.find_element_by_xpath('.//*[@id="action_block"]/button').click() # Клик на "Выполнить"
        time.sleep(3)
        self.driver.find_element_by_xpath('.//input[@id="action-toggle"]').click() # Клик по чекбоксу(ставит галочку)   
        time.sleep(2)
        # self.driver.find_element_by_xpath('.//*[@id="content"]/form/div[2]/input[4]').click() # Клик на "Да, уверен"
        # time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
