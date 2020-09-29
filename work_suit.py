import pytest
from selenium import webdriver
# from Regress_web.test_case_0 import case_0
from Regress_web.test_case_1 import case_1
from Regress_web.test_case_2 import case_2
from Regress_web.test_case_3 import case_3
from Regress_web.test_case_4 import case_4
from Regress_web.test_case_4_1 import case_4_1
from Regress_web.test_case_6 import case_6
from Regress_web.test_case_7 import case_7
from Regress_web.test_case_8 import case_8
from Regress_web.test_case_9 import case_9
from Regress_web.test_case_20 import case_20
from Regress_web.test_case_21 import case_21
from Regress_web.test_case_22 import case_22
from Regress_web.test_case_25 import case_25
from Regress_web.test_case_26 import case_26
from Regress_web.test_case_28 import case_28
from Regress_web.test_case_30 import case_30
# from test_case_12810 import case_12810
import pytest
from Regress_web.page import *


class Test():

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.tvzavr.ru/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.full_screen = 0
        self.page = MainPage(self.driver)
        self.result = ResultPage(self.driver)
        self.prof = Profile(self.driver)
        self.admin = Admin(self.driver)
        self.card = CardFilm(self.driver)

    def teardown(self):
        self.driver.quit()



    def test_case_4(self):
        self.page.loger_info('')
        case_4(self, 0)

