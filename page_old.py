import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import logging


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class ResultPage(BasePage):
    # Найти подтверждающий элемент
    def find_link(self, tag_, class_):
        page = MainPage(self.driver)
        path = './/ttag[@class="cclass"]'
        path_1 = path.replace('ttag', tag_)
        xpath = path_1.replace('cclass', class_)
        # page.waitForElementVisible(xpath, 7)
        time.sleep(2)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        # print('Это суп', soup)
        ls = soup.find(tag_, class_)
        # print(ls)
        return ls

    def find_all_link(self, tag_, class_):
        page = MainPage(self.driver)
        path = './/ttag[@class="cclass"]'
        path_1 = path.replace('ttag', tag_)
        xpath = path_1.replace('cclass', class_)
        page.waitForElementVisible(xpath, 7)
        time.sleep(2)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        ts = soup.find_all(tag_, class_)
        # print(ts)
        return ts

    def find_x(self, tag_, class_):
        # print(self, tag_, class_)
        time.sleep(1)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        ts = soup.find(tag_, class_)
        ls = ts.find('a').get('clip_name')
        # print(ls)
        return ls

    def find_tag(self, tag_):
        # print(self, tag_, class_)
        time.sleep(1)
        table = self.driver.page_source
        soup = BeautifulSoup(table, 'html.parser')
        # print('Это суп', soup)
        ls = soup.find(tag_)
        # print(ls)
        return ls

    def find_all_tag(self, tag_):
        # print(self, tag_, class_)
        time.sleep(1)
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

class Admin(BasePage):

    def click_f(self, name, stap):
        page = MainPage(self.driver)
        step = str(stap)
        if 'No_name' in name:
            page.click_xpath('No_name')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')   #   Admin
        elif 'Клик_список_статус' in name:
            page.click_id('issue_status_id')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_In_Progress_статус' in name:
            page.click_xpath('//*[@id="issue_status_id"]/option[4]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Closed_статус' in name:
            page.click_xpath('//*[@id="issue_status_id"]/option[7]')
            page.click_xpath('.//option[@value="5"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')   #   Admin
        elif 'Клик_Принять' in name:
            page.click_xpath('//*[@id="issue-form"]/input[6]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_первое_письмо' in name:
            self.driver.find_elements_by_xpath('.//a[@class="js-href b-datalist__item__link"]')[0].click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_второе_письмо' in name:
            self.driver.find_elements_by_xpath('.//a[@class="js-href b-datalist__item__link"]')[1].click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')   #   Admin
        elif 'Клик_Ответить' in name:
            page.click_xpath('.//span[@class="b-letter__foot__tab"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Переключение_1_в_iframe' in name:
            self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[1])
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Переключение_2_в_iframe' in name:
            self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Возврат_фокуса_из_iframe' in name:
            self.driver.switch_to.default_content()  # возврат фокуса из iframe
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Отправить_письмо' in name:
            page.click_xpath('//*[@id="b-toolbar__right"]/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/span')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Входящие_mail_ru' in name:
            page.click_xpath('//*[@id="b-nav_folders"]/div/div[1]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Чекбокс_Входящие_mail_ru' in name:
            page.click_xpath('.//div[@class="b-checkbox__box"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Удалить_письма_из_mail_ru' in name:
            page.click_xpath('//*[@id="b-toolbar__right"]/div[2]/div/div[2]/div[2]/div/div[1]/span')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')   #   Admin

class CardFilm(BasePage):

    def click_f(self, name, stap):
        page = MainPage(self.driver)
        step = str(stap)
        if 'No_name' in name:
            page.click_xpath('No_name')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')   #   CardFilm
        elif 'Клик_на_вкладку_Комментарии' in name:
            page.driver.find_element_by_css_selector(
                '#page-content > div.clip-wrap > div.container > div.clip_tabs > div > ul > li:nth-child(3) > a').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_на_вкладку_Трейлеры' in name:
            page.driver.find_element_by_css_selector(
                '#page-content > div.clip-wrap > div.container > div.clip_tabs > div > ul > li:nth-child(4) > a').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_кнопки_просмотр_от_руб' in name:
            page.click_id('clip-pay')
            # page.click_xpath('.//a[@class="txt-c-f clip_pay"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_кнопки_В_избранное' in name:
            page.click_xpath('.//a [@class="clip_actions_item clip_favorite txt-o-6"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен') #   CardFilm
        elif 'Клик_кнопки_Прокат' in name:
            page.click_xpath('.//span[@class="tvz-currency tvz-currency-RUB"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_иконки_найденного_фильма' in name:
            page.click_xpath('.//a[@class="search_form_results_clip_poster-wrap tvz-cap_wrap"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_иконки_избранного_фильма' in name:
            page.click_xpath('.//div [@class="clip-card__title tvz-overflow"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен') #   CardFilm
        elif 'Клик_Play' in name:
            page.click_play()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Stop' in name:
            page.click_stop()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_вкладки_Описание' in name:
            page.click_xpath('//*[@id="page-content"]/div[2]/div[2]/div[4]/div/ul/li[3]/a') #   CardFilm
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_вкладки_Комментарии' in name:
            page.click_xpath('//*[@id="page-content"]/div[2]/div[2]/div[4]/div/ul/li[4]/a')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_вкладки_Серии' in name:
            page.click_xpath('//*[@id="page-content"]/div[2]/div[2]/div[4]/div/ul/li[2]/a')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_2_ой_Серии_1_го_сезона' in name:
            page.click_xpath('//*[@id="episodes-wrapper-22693"]/div/div[2]/a/div[1]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен') #   CardFilm
        elif 'Клик_кнопки_Убрать_из_избранного' in name:
            self.driver.find_element_by_xpath('.//a[@class="clip_actions_item clip_favorite txt-o-6 clip_actions_item-active"]').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')

class Profile(BasePage):
    def click_f(self, name, step_int):
        result = ResultPage(self.driver)
        page = MainPage(self.driver)
        step = str(step_int)
        if 'No_name' in name:
            page.click_xpath('No_name')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен') # Начальный экран приложения
        elif 'Клик_Регистрация' in name:
            page.click_a('Регистрация')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_Зарегистрироваться' in name:
            page.click_id('register-email-submit')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_phone_Зарегистрироваться' in name:
            self.driver.find_element_by_css_selector('#register-submit').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Аватарка_М' in name:
            page.click_ava('male')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_Аватарка_Ж' in name:
            page.click_ava('female')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_поиска_Лупа' in name:
            page.click_id('header-search-btn')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Подписки_и_покупки' in name:
            self.driver.find_element_by_xpath('.//a[@class="profile-menu__link"][contains(., "Подписки и покупки")]').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_Выйти' in name:
            page.click_xpath('.//button[@class="profile-menu__logout js-profile-logout"]')
            # page.click_a('Выход')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_Пополнить' in name:
            page.click_xpath('.//a[@class="profile_balance_add btn btn-light btn-block js-replenishment"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_Личный_счет' in name:
            page.click_xpath(
                './/a[@class="payment-form__link payment-form__link_tvzavrwallet tvz-tabs-t1_link tvz-tabs-t1-1_link"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_Оплатить' in name:
            self.driver.find_element_by_css_selector('#block_tvzavrwallet > button').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Настройки_профиля' in name:
            page.click_a('Настройки профиля')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_день_рождения' in name:
            page.click_id('select2-birthday-day-container')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Клик_месяц_рождения' in name:
            page.click_id('select2-birthday-month-container')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_год_рождения' in name:
            page.click_id('select2-birthday-year-container')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_выбран_пол' in name:
            self.driver.find_element_by_xpath('.//span[@class="tvz-icon tvz-icon-record"]').click()     # Profile
            # page.click_xpath('.//span[@class="tvz-icon tvz-icon-record"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Ввод_дня_рождения' in name:
            self.driver.find_element_by_css_selector('#birthday-day > option:nth-child(5)').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Ввод_месяца_рождения' in name:
            self.driver.find_element_by_css_selector('#birthday-month > option:nth-child(5)').click()
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')     # Profile
        elif 'Ввод_года_рождения' in name:
            page.click_xpath('.//option[@value="1990"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Снятие_галочки_с_подписки' in name:
            page.click_xpath('.//span[text()="Да, я хочу получать подписку с обновлениями, акциями и подарками"]')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Снятие_галочки_с_продолжения_просмотра' in name:
            page.click_xpath('.//span[text()="Продолжать просмотр с места остановки"]')     # Profile
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Сохранить' in name:
            page.click_button('Сохранить')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Избранное' in name:
            page.click_a('Избранное')
            page.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')       # Profile


class MainPage(BasePage):
    def click_f(self, name, stap):
        step = str(stap)
        if 'No_name' in name:
            self.driver.find_element_by_xpath('No_name').click()
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_прокрутки_слайда_вправо' in name:
            self.click_xpath(
                './/button[@class="slider__navigation slider__navigation_next js-slider-navigation js-slider-navigation-next"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_прокрутки_слайда_влево' in name:
            self.click_xpath(
                './/button[@class="slider__navigation slider__navigation_prev js-slider-navigation js-slider-navigation-prev"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_поиска_Лупа' in name:
            self.driver.find_element_by_css_selector('#header-search-btn').click()      #   MainPage
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_кнопки_крестик' in name:
            self.click_xpath('.//span[@class="tvz-icon tvz-icon-close"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Новинки' in name:
            # self.click_a("Новинки")
            self.click_xpath('.//a[@class="header__link"][contains(., "Новинки")]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Показать_еще' in name:
            self.click_button('Показать еще')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Подписки' in name:
            self.click_xpath('.//a[@class="header__link"][contains(., "Подписки")]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_Подписка_Отключи_рекламу' in name:
            self.click_a('Подписка «Отключи рекламу на tvzavr!»')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Подписка_Детская' in name:
            self.click_a('Подписка «Детская»')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Бесплатно' in name:
            self.click_xpath('.//a[@class="header__link"][contains(., "Бесплатно")]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_Каталог' in name:
            self.click_xpath('.//a[@class="header__link"][contains(., "Каталог")]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Жанр' in name:
            self.click_xpath('.//button[@class="filter__toggle"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_советский_жанр' in name:
            self.click_xpath('.//li[@data-tag-name="советский"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_Сериалы' in name:
            self.click_a('Сериалы')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Вход' in name:
            self.click_enter()
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_Войти_auth' in name:
            self.driver.find_element_by_css_selector('#auth-submit').click()
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'По_номеру_телефона' in name:
            self.click_xpath('.//a[@data-target="register-phone-tab"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_Подборки' in name:
            self.click_xpath('.//a[@class="header__link"][contains(., "Подборки")]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Обратная_связь' in name:
            self.click_button('Обратная связь')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_Отправить_сообщение' in name:
            self.click_button('Отправить')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Редактировать' in name:
            self.click_a('Редактировать')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_первого_фильма' in name:
            self.click_xpath('.//div[@class="owl-item active"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Клик_стрелка_Вниз' in name:
            self.driver.find_element_by_tag_name("body").send_keys(Keys.DOWN)
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_постер_первого_фильма' in name:
            self.click_xpath('.//div [@class="catalog__clip tvz-col-2 col-sm-3 tvz-col-5 col-lg-2"]')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Клик_постер_сериала' in name:
            self.click_xpath('//*[@id="search-form-clips"]/div[1]/div[1]/a')
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')
        elif 'Переход_вниз_страницы' in name:
            self.driver.find_element_by_tag_name("body").send_keys(Keys.END)
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage

    def send_f(self, name, text, stap):
        step = str(stap)
        if 'No_name' in name:
            self.driver.find_element_by_xpath('No_name').click()
            self.loger_info('Шаг ' + step + '. Клик ' + name + ' произведен')      #   MainPage
        elif 'Ввод_псевдонима' in name:
            self.driver.find_element_by_id('name').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_в_строку_поиска' in name:
            self.send_id('search-input', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_2_в_строку_поиска' in name:
            self.send_id('header-search-input', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_логина' in name:
            self.send_name('email', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_name_логина' in name:
            self.send_name('login', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')      #   MainPage
        elif 'Ввод_пароля' in name:
            self.driver.find_element_by_css_selector('#register-email-password').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_профиль_old_пароля' in name:
            self.driver.find_element_by_id('password').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_профиль_new_пароля' in name:
            self.driver.find_element_by_id('password1').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_профиль_com_пароля' in name:
            self.driver.find_element_by_id('password2').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_номера_телефона_reg' in name:
            self.send_name('phone', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_номера_телефона_auth' in name:
            self.driver.find_element_by_css_selector('#auth-login').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_СМС_пароля_reg' in name:
            self.send_name('code', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_из_СМС_пароля_auth' in name:
            self.driver.find_element_by_css_selector('#auth-password').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_суммы_пополнения_счета' in name:
            self.driver.find_element_by_css_selector('#modals-payment_info > div.payment-form__amount > input').send_keys(text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'feedback_имя_пользователя' in name:
            self.send_id('feedback-form_name', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'feedback_e_mail_пользователя' in name:
            self.send_id('feedback-form_email', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'feedback_сообщение_пользователя' in name:
            self.send_id('feedback-form_decr', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_ответа_пользователю' in name:
            self.send_id('issue_notes', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')
        elif 'Ввод_текста_ответа_пользователя' in name:
            self.send_id('tinymce', text)
            self.loger_info('Шаг ' + step + ' '+ name + ' ' + text + ' произведен')



    #  Функция клик пропуска фулл скрина test case 9 + all Sony
    def click_button(self, bc):
        button_xpath = ('.//button[text()="%s"]' % bc)
        # self.loger_info(button_xpath)
        self.driver.find_element_by_xpath(button_xpath).click()

    #  Функция клик кнопок верхнего меню
    def click_div(self, dep):
        up_xpath = ('.//div[text()="%s"]' % dep)
        self.waitForElementClickable(up_xpath, 30)
        time.sleep(1)
        self.driver.find_element_by_xpath(up_xpath).click()
        # print('Клик', dep)
        return

    #  Функция клик вкладок
    def click_li(self, dep):
        li_xpath = ('.//li[text()="%s"]' % dep)
        self.waitForElementClickable(li_xpath, 30)
        time.sleep(1)
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
        time.sleep(1)
        self.driver.find_element_by_xpath(span_xpath).click()
        # print('Клик', dep)

    def click_id(self, dep):
        self.waitForIDVisible(dep, 30)
        self.driver.find_element_by_id(dep).click()
        # print('Клик', dep)

    def click_name(self, dep):
        self.waitForNameVisible(dep, 30)
        self.driver.find_element_by_name(dep).click()
        # print('Клик', dep)

    def click_xpath(self, xpath):
        self.waitForElementClickable(xpath, 30)
        self.driver.find_element_by_xpath(xpath).click()
        # print('Клик', dep)

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
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath).click()
        # self.driver.find_element_by_css_selector(css_sel).click()
        # print('Клик', dep)

    def click_enter(self):
        self.click_xpath('.//button[@class="header__login"]')

    def click_ava(self, sex):
        self.click_xpath('.//span[@class="header__avatar tvz-avatar_cap __useravatar tvz-avatar_cap-%s"]' % sex)

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

    # Функция ввода логина
    def login(self, name, logi):
        self.waitForNameVisible(name, 40)
        self.driver.find_element_by_name(name).send_keys(logi)
        return

    # Функция ввода
    def send_id(self, d_id, txt):
        self.waitForIDVisible(d_id, 30)
        self.driver.find_element_by_id(d_id).send_keys(txt)
        return

    def send_name(self, d_name, txt):
        self.waitForNameVisible(d_name, 30)
        self.driver.find_element_by_name(d_name).send_keys(txt)
        return

    # Функция ввода
    def input(self, dclass, data):
        li_xpath = ('.//input[@class="%s"]' % dclass)
        # self.waitForElementClickable(li_xpath, 80)
        time.sleep(1)
        self.driver.find_element_by_xpath(li_xpath).send_keys(data)

    def rand_mail(self, lit):
        d = str(datetime.today())
        ds = d.replace('-', '')
        d = ds.split(':')[0]
        d_2 = ds.split(':')[1]
        d_3 = d.replace(' ', '')
        rand = d_3 + d_2
        # self.loger_info(rand)
        random_mail = 'tvzavrtest' + rand + lit + '@regress.ru'
        return (random_mail, rand)

    def code_phone(self, phone):
        self.loger_info('Получение кода на телефон:  ' + phone)
        url = 'http://www.tvzavr.ru/api/3.1/sms/send_confirm_code?phone=' + str(phone) + '&entity=empty&prv=smsfake_tvz'
        # url = 'http://www.tvzavr.ru/api/3.1/sms/send_confirm_code?phone=' + str(phone) + '&entity=empty&prv=smstest_tvz'
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
        chrome_options.add_argument(
            "user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")  # Запуск браузера с сохраненным профилем
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://app.mysms.com/")
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.driver.find_element_by_xpath('.//div[@class="gwt-Label"]').click()  # Новое сообщение
        time.sleep(1)
        self.driver.find_element_by_xpath('.//input[@class="recipientTextBox"]').send_keys(phone)
        time.sleep(1)
        self.driver.find_element_by_xpath('.//div[@class="textarea"]').send_keys(message)
        time.sleep(1)
        self.driver.find_element_by_xpath('.//button[@class="styledButton sendButton sim dropdown"]').click()
        logging.info("Клик 'Отправить' произведен, СМС подтверждения отправлено")
        self.driver.close()
        return

    def login_google(self, emailgo, passok):
        time.sleep(1)
        self.send_id('identifierId', emailgo)
        print('Ввод логина Google', emailgo, 'произведен')
        time.sleep(1)
        # Шаг 29
        self.driver.find_element_by_css_selector('#identifierNext > content > span').click()
        print(' Клик кнопки "Далее" произведен')
        time.sleep(1)
        # Шаг 30
        self.driver.find_element_by_name('password').send_keys(passok)
        # self.driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(passok)
        print(' Ввод пароля произведен')
        time.sleep(1)
        # Шаг 31
        self.click_xpath('.//span[@class="RveJvd snByac"][contains(., "Далее")]')
        print(' Клик кнопки "Далее" произведен')
        time.sleep(8)
        return

    def login_tvzavr(self, email, passw, sex):
        result = ResultPage(self.driver)
        prof = Profile(self.driver)
        self.waitForElementVisible('.//button[@class="header__login"]', 7)
        resic = result.find_link("button", "header__login")
        if "Вход" not in resic:
            if sex == 'male':
                prof.click_f('Клик_Аватарка_М', 1)
            else:
                prof.click_f('Клик_Аватарка_Ж', 1)

            time.sleep(2)
            self.driver.find_element_by_xpath('.//button[@class="profile-menu__logout js-profile-logout"]').click()
            time.sleep(1)
        else:
            # Шаг 1 Нажать в шапке на кнопку "Вход".')
            self.click_enter()
            self.loger_info('Шаг 2 Клик "Вход" произведен')
            time.sleep(2)
            # Шаг 2
            self.send_id('auth-login', email)
            self.loger_info('Шаг 3 Ввод email' + email + 'произведен')
            # Шаг 3
            self.driver.find_element_by_id('auth-password').send_keys(passw)
            self.loger_info('Шаг 4 Введен пароль ' + passw)
            # Шаг 4
            self.driver.find_element_by_id('auth-submit').click()
            self.loger_info('Шаг 5 Клик Войти произведен')
            # time.sleep(10)
            # try:
            #     self.click_f('Клик_кнопки_крестик', 6)
            # except:
            #     print('нет акции мицубиси')
            # Шаг 5
            if sex == 'male':
                prof.click_f('Клик_Аватарка_М', 7)
            else:
                prof.click_f('Клик_Аватарка_Ж', 8)
            time.sleep(3)
        return

    def login_mailru(self, emailru, passw):
        self.send_id('mailbox:login', emailru)
        self.loger_info('Ввод логина на mail.ru ' + emailru + 'произведен')
        time.sleep(1)
        self.send_id('mailbox:password', passw)
        self.loger_info('Ввод пароля на mail.ru произведен')
        time.sleep(1)
        self.driver.find_element_by_xpath('.//input[@class="o-control"]').click()
        self.loger_info('Клик кнопки "Войти" на mail.ru произведен')
        time.sleep(5)

    def registration(self, email, passw):
        result = ResultPage(self.driver)
        prof = Profile(self.driver)
        resic = result.find_link("button", "header__login tvz-unauthorized")
        if "Вход" not in resic:
            prof.click_f('Клик_Аватарка_М', 1)
            self.loger_info('Шаг 0 Клик на аватарку пользователя произведен')
            self.driver.find_element_by_xpath('.//button[@class="profile-menu__logout js-profile-logout"]').click()
            time.sleep(1)
        else:
            self.click_enter()
            self.loger_info('Шаг 1 Клик "Вход" произведен')
            # Шаг 2
            self.click_a('Регистрация')
            self.loger_info('Шаг 2 Клик "Регистрация" произведен')
            time.sleep(1)
            # Шаг 3
            self.login('email', email)
            print('Шаг 3 Ввод логина', email, 'произведен')
            # Шаг 4
            self.driver.find_element_by_css_selector('#register-email-password').send_keys(passw)
            # page.login('password', passw)
            self.loger_info('Шаг 4 Ввод пароля произведен')
            time.sleep(1)
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

            time.sleep(1)

    def input_card(self, number, month, year, name, cvv):
        result = ResultPage(self.driver)
        self.driver.find_elements_by_xpath('.//input[@class="payment-cloudpayments__field tvz-input tvz-input-t1 js-input"]')[0].send_keys(number)
        self.loger_info('Шаг 10 Ввод номера карты произведен ' + number)
        self.driver.find_elements_by_xpath('.//span[@class="select2-selection select2-selection--single tvz-select"]')[0].click()
        self.driver.find_element_by_xpath('.//option[@value="%s"]' % month).click()
        self.loger_info('Ввод месяца карты произведен')
        self.driver.find_elements_by_xpath('.//span[@class="select2-selection select2-selection--single tvz-select"]')[1].click()
        self.driver.find_element_by_xpath('.//option[@value="%s"]' % year).click()
        self.loger_info('Ввод года карты произведен')
        # Заполнить поле "Имя держателя" - Ivanov Ivan
        self.driver.find_elements_by_xpath('.//input[@class="payment-cloudpayments__field tvz-input tvz-input-t1 js-input"]')[1].send_keys(name)
        self.loger_info('Ввод имени держателя карты произведен')
        # Заполнить поле "CVV код" - 630
        self.driver.find_element_by_xpath('.//input[@class="payment-cloudpayments__field payment-cloudpayments__field_cvc tvz-input tvz-input-t1 js-input"]').send_keys(cvv)
        self.loger_info('Ввод CVV код карты произведен')
        # Снять галочку "Сохранить данные карты"
        self.driver.find_element_by_xpath('.//label[@class="payment-cloudpayments__remember tvz-checkbox no-us-select"]').click()
        self.loger_info('Снятие галочки в чек-боксе"Сохранить данные карты" произведено')
        #  Нажать кнопку "Оплатить"clip-watch
        self.driver.find_element_by_xpath('.//button[@class="payment-cloudpayments__pay btn js-buy-button"]').click()
        self.loger_info('Клик "Оплатить" произведен')
        # message = str(result.find_link("section", "tvz-alerts tvz-animation-fadeOut"))
        # self.loger_info('Сообщение внизу формы оплаты:')
        # self.loger_info('message:' + message)

    def delete_mails(self, emailgo, passgo):
        # self.driver.get('https://mail.google.com')
        self.loger_info('Шаг 5 Переход на gmail.com произведен')
        # self.login_google(emailgo, passgo)
        time.sleep(1)
        # self.driver.get('https://mail.google.com/mail/u/0/#inbox')
        # Удаление письма из почты
        self.click_xpath('.//div[@class="J-J5-Ji J-JN-M-I-Jm"]')
        # self.driver.find_element_by_id(':3d').click()
        self.loger_info('Поставлена галочка чекбокс - выбор письма')
        self.click_xpath('//*[@id=":5"]/div/div[1]/div[1]/div/div/div[2]/div[3]')
        # self.click_xpath('.//div[@class="T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA"]')
        self.loger_info('Клик кнопки "Удалить" письмо на gmail.com произведен')
        time.sleep(2)

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

    def scype_send_web(self, login, passw, text):
        result = ResultPage(self.driver)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        self.driver = webdriver.Chrome(options=options)
        time.sleep(10)
        self.driver.get("https://web.skype.com/ru/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.loger_info(' Переход в Skype произведен')
        self.send_name('loginfmt', login)
        self.click_id('idSIButton9')
        time.sleep(1)
        self.send_name('passwd', passw)
        self.loger_info('Ввод Skype пароля произведен')
        time.sleep(1)
        self.click_xpath('//*[@id="idSIButton9"]')
        self.loger_info('Клик Войти произведен')

        time.sleep(5)
        self.click_xpath('.//span[@class="topic"][contains(., "Деплоймент")]')
        self.loger_info('Переход в чат Деплоймент произведен')
        time.sleep(2)
        self.click_xpath('.//textarea[@id="chatInputAreaWithQuotes"]')
        self.loger_info('Клик в чат Деплоймент произведен')
        self.driver.find_element_by_id('chatInputAreaWithQuotes').send_keys(text)
        self.loger_info('Ввод текста в чат Деплоймент произведена')
        # self.send_id('chatInputAreaWithQuotes', text)
        time.sleep(2)
        self.click_xpath('//*[@id="swxContent1"]/swx-navigation/div/div/div/label/div/div/div[2]/div[2]/div/swx-button/button')
        self.loger_info('Отправка текста в чат Деплоймент произведена')
        self.driver.close()
