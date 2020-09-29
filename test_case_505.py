from Regress_web.page import *
import os

import warnings
import pytest


    
def case_505(self, full_screen):
    self.page.loger('\n Запуск тест кейса 505 \n')
    time.sleep(1)
       
    self.driver.get("https://partners-beta.movieschain.io/")
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//button[@class="header__button button-login"]').click()
    time.sleep(1)

    self.driver.find_element_by_xpath('.//input[@type="email"]').send_keys('testmailtvzavr@mail.ru')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//input[@type="password"]').send_keys('12345678Aleh')
    time.sleep(1)

    self.driver.find_element_by_xpath('.//button[@id="signIn"]').click()
    time.sleep(2)

    target = self.driver.find_element_by_xpath('.//button[@class="button-main button-main_margin"]')
    target.location_once_scrolled_into_view
    time.sleep(2)
    
    self.driver.find_element_by_xpath('//input[@type="file"]').send_keys('C:\\logo\image.jpeg')
    time.sleep(2)

    self.driver.find_elements_by_xpath('//input[@type="file"]')[1].send_keys('C:\\logo\picture.jpeg')

    
    

