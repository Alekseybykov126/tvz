from .page import *

def case_4_2(self, full_screen):
    self.page.loger_info('\n Запуск    Тест кейс № 4_2 tvweb_new-4_2: Проверка перехода по ссылкам на соцсети внизу страницы \n')
    def setup_method(self, method):
        self.driver = webdriver.Chrome()

    self.driver.get("https://www.tvzavr.ru/") 

    self.page.click_f('Переход_вниз_страницы', 1)
    time.sleep(3)
    self.page.click_f('Переход_вниз_страницы', 2)
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="footer__socials"]', 10)
    res_txt = str(self.result.find_all_link("div", "footer__socials"))
    assert ('tvzavr в Одноклассниках') in res_txt
    assert ('tvzavr в ВКонтакте') in res_txt
    assert ('tvzavr в Facebook') in res_txt
    assert ('tvzavr в Twitter') in res_txt
    assert ('tvzavr в Instagram') in res_txt
    assert ('tvzavr в Youtube') in res_txt
    assert ('tvzavr в Coub') in res_txt
    self.page.loger('Шаг 3. Наличие всех ссылок на соцсети подтверждено')
    time.sleep(2)

    # Одноклассники
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в Одноклассниках"]').click()
    self.driver.switch_to.window(self.driver.window_handles[1]) # Переключение на вторую вкладку
    time.sleep(2)
    
    url1 = self.driver.current_url    # Получение url
    if url1 == 'https://ok.ru/tvzavr':
        self.page.loger('Шаг 4. Переход по ссылке на "Одноклассники" подтверждён')
    else:
        assert(), "Переход на Одноклассники не произведён"
    time.sleep(2)

    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    # Вконтакте
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в ВКонтакте"]').click()
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    
    url1 = self.driver.current_url
    if url1 == 'https://vk.com/tvzavr':
        self.page.loger('Шаг 5. Переход по ссылке на "Вконтакте" подтверждён')
    else:
        assert(), "Переход на Вконтакте не произведён"
    time.sleep(2)
    
    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)
    
    # Facebook
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в Facebook"]').click()
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    
    url1 = self.driver.current_url
    if url1 == 'https://www.facebook.com/tvzavr':
        self.page.loger('Шаг 6. Переход по ссылке на "Facebook" подтверждён')
    else:
        assert(), "Переход на Facebook не произведён"
    time.sleep(2)
    
    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)
    
    # Twitter
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в Twitter"]').click()
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    
    url1 = self.driver.current_url
    if url1 == 'https://twitter.com/tvzavr':
        self.page.loger('Шаг 7. Переход по ссылке на "Twitter" подтверждён')
    else:
        assert(), "Переход на Twitter не произведён"
    time.sleep(2)
    
    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)
    
    # Instagram
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в Instagram"]').click()
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    
    url1 = self.driver.current_url
    if url1 == 'https://www.instagram.com/tvzavr.ru/':
        self.page.loger('Шаг 8. Переход по ссылке на "Instagram" подтверждён')
    else:
        assert(), "Переход на Instagram не произведён"
    time.sleep(2)
    
    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)
    
    # Youtube
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в Youtube"]').click()
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    
    url1 = self.driver.current_url
    if url1 == 'https://www.youtube.com/tvzavr':
        self.page.loger('Шаг 9. Переход по ссылке на "Youtube" подтверждён')
    else:
        assert(), "Переход на Youtube не произведён"
    time.sleep(2)
    
    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)
    
    # Coub
    self.driver.find_element_by_xpath('.//a[@title="tvzavr в Coub"]').click()  
    self.driver.switch_to.window(self.driver.window_handles[1])
    time.sleep(2)
    
    url1 = self.driver.current_url
    if url1 == 'https://coub.com/tvzavr.ru':
        self.page.loger('Шаг 10. Переход по ссылке на "Coub" подтверждён')
    else:
        assert(), "Переход на Coub не произведён"
    time.sleep(2)
    
    self.driver.close()
    time.sleep(1)
    self.driver.switch_to.window(self.driver.window_handles[-1])
    time.sleep(2)

    self.driver.quit()