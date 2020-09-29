from .page import *

def case_5_1(self, full_screen):
    time.sleep(1)
    self.page.loger('\n Запуск Тест кейс № 5_1 tvweb_new-5_1: Настройка профиля \n')
    
    email = self.page.rand_mail('7')[0]
    psevdonim = email.split('@')[0]
    passw = '333333'
    time.sleep(3)
    
    time.sleep(2)
    self.page.click_f('Клик_Вход', 1)
    time.sleep(2)
    
    self.prof.click_f('Клик_Регистрация', 2)
    time.sleep(2)
    
    #self.page.send_f('Ввод_логина', email, 3)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__address textbox"]').send_keys(email)
    time.sleep(2)
    
    #self.page.send_f('Ввод_пароля', passw, 4)
    self.driver.find_element_by_xpath('.//input[@class="email-registration__password textbox"]').send_keys(passw)
    time.sleep(2)
    
    self.prof.click_f('Клик_Зарегистрироваться', 5)
    time.sleep(2)
    
    #self.page.waitForElementVisible('.//a[@title="Смотреть Новинки кино онлайн"]', 30)
    self.page.waitForElementVisible('.//a[@class="header__link"]', 30)
    
    self.prof.click_f('Клик_значок_нового_пользователя', 7)
    time.sleep(2)

    remember_name = self.driver.find_element_by_xpath("//div[@class='profile-menu__name __username']") # запоминание имени пользователя
    remember_name = remember_name.get_attribute('innerHTML')
    text = remember_name
    time.sleep(3)

    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 8) # Проверка авторизации пользователя"
    resic = str(self.result.find_link("div", "profile-menu__name __username"))
    assert (email) in resic
    self.page.loger('Авторизация зарегистрированного пользователя с е-майлом ' + email + ' подтверждена')
    time.sleep(2)
    
    self.prof.click_f('Клик_Настройки_профиля', 9)
    time.sleep(5)
    
    self.prof.click_f('Клик_крестик_всплывшего_окна_тройка', 10)
    time.sleep(3)

    self.page.send_f('Ввод_псевдонима', psevdonim, 11)
    time.sleep(2)
    
    self.prof.click_f('Клик_день_рождения', 12)
    time.sleep(2)

    self.prof.click_f('Ввод_дня_рождения', 13)
    time.sleep(2)

    self.page.loger_info('Шаг 9 Ввод дня рождения произведен')
    time.sleep(2)
    
    self.prof.click_f('Клик_месяц_рождения', 14)
    time.sleep(2)

    self.prof.click_f('Ввод_месяца_рождения', 15)
    time.sleep(2)
   
    self.prof.click_f('Клик_год_рождения', 16)
    time.sleep(2)

    self.prof.click_f('Ввод_года_рождения', 14)
    time.sleep(2)
    
    self.prof.click_f('Клик_выбран_пол', 15)
    time.sleep(2)
    
    self.prof.click_f('Клик_Снятие_галочки_с_подписки', 16)
    time.sleep(3)
    
    self.prof.click_f('Клик_Сохранить', 18)
    time.sleep(4)

    self.prof.click_f('Клик_значок_нового_пользователя', 19)
    time.sleep(2)

    self.prof.click_f('Клик_Подписки', 20)
    time.sleep(5)

    self.page.loger_info('Клик "Подписки и покупки" произведен')
    time.sleep(2)

    self.page.loger_info('Шаг 16 Обновление страницы произведено')
    time.sleep(5)

    self.prof.click_f('Клик_значок_нового_пользователя', 21)
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 22)
    resic = str(self.result.find_link("div", "profile-menu__name __username"))
    assert (psevdonim) in resic
    self.page.loger('Псевдоним ' + psevdonim + ' подтвержден')
    time.sleep(2)

    self.prof.click_f('Клик_переход_в_настройки', 23)
    time.sleep(5)
    
    self.page.send_f('Ввод_профиль_old_пароля', '333333', 25)
    time.sleep(2)
    
    self.page.send_f('Ввод_профиль_new_пароля', '444444', 26)
    time.sleep(2)
    
    self.page.send_f('Ввод_профиль_rep_пароля', '444444', 27)
    time.sleep(2)
    
    self.prof.click_f('Клик_Сохранить', 28)
    time.sleep(4) 

    self.page.click_f('Клик_Вход', 29) # Проверка авторизации по новому паролю
    time.sleep(5)

    self.driver.find_element_by_xpath('.//input[@class="authorization__login textbox"]').send_keys(email)
    time.sleep(2)
    
    self.driver.find_element_by_xpath('.//input[@class="authorization__password textbox"]').send_keys(444444)
    time.sleep(2)

    self.page.click_f('Клик_Войти_auth', 32)
    time.sleep(5)

    self.page.waitForElementVisible('.//div[@class="owl-item active"]', 10) # Проверка появления слайдеров, как подтверждение авторизации
    time.sleep(3)

    self.prof.click_f('Клик_значок_пользователя', 33)  
    time.sleep(2)

    self.page.waitForElementVisible('.//div[@class="profile-menu__name __username"]', 34) # Проверка авторизации пользователя с новым паролем
    resic = str(self.result.find_link("div", "profile-menu__name __username"))
    assert (psevdonim) in resic
    self.page.loger('Авторизация зарегистрированного пользователя с е-майлом ' + psevdonim + ' подтверждена')
    time.sleep(3)

    

    self.page.delete_uzer(remember_name)
    time.sleep(3)

    self.driver.quit()