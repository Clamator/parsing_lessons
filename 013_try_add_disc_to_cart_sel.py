from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
from multiprocessing import Pool
# https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html
from selenium.webdriver.common.by import By

discogs_login_page = "https://discogs.com/login"


class TestFunc(object):

    def __init__(self):
        # тут ниже идет настройка, чтобы сайт не видел,что используется вебдрайвер
        option = Options()
        option.add_argument("--disable-blink-features=AutomationControlled")
        option.headless = True  # , если скрывать браузер, пишет email_field = self.driver.find_element_by_id("username")
        # если поставить xpath, то не работает все равно
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get(discogs_login_page)

    def login(self, username, password):
        # email_field = self.driver.find_element_by_id("username")
        # email_field.send_keys(username)
        # sleep(1)
        # password_field = self.driver.find_element_by_id("password")
        # password_field.send_keys(password)
        # sleep(1)
        # login_button = self.driver.find_element_by_css_selector('button[type="submit"]')
        # login_button.click()
        # sleep(0.5)
        # это список дисков
        self.driver.get('https://www.discogs.com/ru/sell/list?master_id=484900&ev=mb')
        for cookies in pickle.load(open('session', 'rb')):
            self.driver.add_cookie(cookies)
        self.driver.refresh()
        # это ссылка на мою коллекцию v
        # self.driver.get('https://www.discogs.com/ru/user/Clamator/collection')
        sleep(0.5)

        # поиск дисков только из России
        button = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[5]/div[2]/ul/li[1]/ul/li[6]/a/span[2]')
        self.driver.execute_script("arguments[0].click();", button)


        add_to_cart_links = []
        all_discs = self.driver.find_elements_by_class_name('shortcut_navigable ')
        for disc in all_discs:
            # link = disc.find_element(By.XPATH, "//a[@class='button button-green cart-button ']").get_attribute('href')
            # <a class="button button-green cart-button "
            # название класса было через пробелы, взял первое слово, а - это тег.
            try:
                link = disc.find_element_by_css_selector('a.button').get_attribute('href')
                # self.driver.execute_script("arguments[0].click();", link)
                if 'cart' in link:
                    add_to_cart_links.append(link)
            except:
                link = ''

        # отправить диско в корзину - работает
        # for el in add_to_cart_links:
        #     self.driver.get(el)




if __name__ == '__main__':
    username = 'Clamator'
    password = 'Munroe23'
    TestFunc().login(username, password)

# driver.get(url=url) #В переменной url ваша страница
# driver.implicitly_wait(5) #В скобках количество секунд ожидания, если страница подгрузится быстрей то ожидание прервется и код продолжит выполнятся
