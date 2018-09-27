import time
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
#import bs4
#from bs4 import BeautifulSoup
#import requests
#from requests.urllib import urlretrieve


class Account():

    def __init__(self, ID, password):
        self.id = ID
        self.password = password

class Login():

    LINK = r"https://www.instagram.com/accounts/login/?source=auth_switcher"
    HOME = r"https://www.instagram.com"

    def __init__(self, path):
        #self.binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        #self.driver = webdriver.Firefox(firefox_binary=self.binary)
        #self.profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Chrome(path)


    def insta_login(self, account):
        self.driver.get(Login.LINK)

        self.driver.find_element_by_name("username").send_keys(account.id)
        self.driver.find_element_by_name("password").send_keys(account.password)

        time.sleep(.5)
        
        log_in = self.driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
        cookies = self.driver.get_cookies()
        time.sleep(2)
        self.driver.get(Login.HOME)
        self.account_data(account.id)
        #time.sleep(50)
        #self.driver.quit()

    def account_data(self, account):
        self.driver.get(Login.HOME + "/" + account)
        self.driver.find_element_by_class_name("KL4Bh")
        
    
    def grab_image(self):
        pass
        self.driver.find_

class Download():

    def grab_image(self, link):
        pass
        

    def grab_():
        pass
        

def main():
    #account_name, account_password = sys.argv[1:]
    
    user = "lukeneedshelp"
    password = "luke19940926help"
    account = Account(user, password)
    path = "C:\\Users\\George Burac\\Desktop\\chromedriver.exe"
    test = Login(path)
    test.insta_login(account)
  

if __name__ == "__main__":
    main()

