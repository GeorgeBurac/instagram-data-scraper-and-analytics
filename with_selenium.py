import time
import selenium
from selenium import webdriver
import sys
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from urllib.request import urlretrieve


#import bs4
#from bs4 import BeautifulSoup
#from requests.urllib import urlretrieve


class Account():

    def __init__(self, ID, password):
        self.id = ID
        self.password = password

class Login():

    SCROLL_SCRIPT = "window.scrollTo(0, document.body.scrollHeight);"
    
    LINK = r"https://www.instagram.com/accounts/login/?source=auth_switcher"
    HOME = r"https://www.instagram.com"

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)


    def insta_login(self, account):
        self.driver.get(Login.LINK)

        self.driver.find_element_by_name("username").send_keys(account.id)
        self.driver.find_element_by_name("password").send_keys(account.password)

        time.sleep(.5)
        
        log_in = self.driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
        time.sleep(2)
        self.driver.get(Login.HOME)
        self.account_data(account.id)
        
        
    def account_data(self, account):
        Link_Error = """Message: stale element reference: element is not attached to the page document
  (Session info: chrome=69.0.3497.100)
  (Driver info: chromedriver=2.42.591088 (7b2b2dca23cca0862f674758c9a3933e685c27d5),platform=Windows NT 10.0.17134 x86_64)"""
        self.driver.get(Login.HOME + "/" + account)
        posts_count = int(str(self.driver.find_element_by_class_name("g47SY ").text))
        print(posts_count)
        profile_name = self.driver.find_element_by_tag_name("h1").get_attribute("title")
        print(profile_name)
        posts = []
        img_links = []
        alts = []
        video_links = []

        times_to_scroll = (posts_count // 4)
        scrolls = 0
        while scrolls < times_to_scroll:
            self.driver.execute_script(Login.SCROLL_SCRIPT)
            time.sleep(.2)
            get_img_links(img_links)
            get_alts(alts)
            grab_videos(video_links)
            
                  scrolls += 1
        print(len(img_links))
        print(len(alts))

    def get_img_stories(self, img_link_stories):
        new_stories = self.driver.find_elements_by_class_name("qFq_l")
        for story in new_stories:
            story.click()
            button_next = self.driver.find_element_by_class_name("  _6CZji")
            while button_next:
                link = self.driver.find_element_by_class("FFVAD").get_attribute("src")
                if link not in stories:
                    stories.append(link)
                try:
                    button_next = self.driver.find_element_by_class_name("  _6CZji")
                    button_next.click()
                except:
                    button_next = False
                
            
    def get_story(self):
        profile_pic = self.driver.find_element_by_class_name("_6q-tv").click()
        time.sleep(.2)
        try:
            img_link = self.driver.find_element_by_class_name("y-yJ5").get_attribute("src")
        except:
            time.sleep(1)
            img_link = self.driver.find_element_by_class_name("y-yJ5").get_attribute("src")
            
            
        try:
            video_link = self.driver.find_element_by_class_name("y-yJ5  OFkrO ").get_attribute("src")
        

                                                                           
    def get_img_links(self, img_links):
        new_links = self.driver.find_elements_by_class_name("FFVAD")
        for item in new_links:
            try:
                link = item.get_attribute("src")
                if link not in img_links:
                    img_links.append(link)
                    print(link)
            except Exception as e:
                if e == Link_Error:
                    time.sleep(1)
                    link = item.get_attribute("src")
                    if link not in img_links:
                        img_links.append(link)
                        print(link)

    def grab_videos(self, video_links):
        new_videos = self.driver.find_elements_by_class_name("tWeCl")
        for item in new_videos:
            try:    
                video_link = item.get_attribute("src")
                if video_link not in video_links:
                    video_links.append(video_link)
            except:
                continue
                
    
    def get_alts(self, alts):
        new_descriptions = self.driver.find_elements_by_class_name("KL4Bh")
        for desc in new_descriptions:
            try:
                alt = desc.get_attribute("alt")
                if alt not in alts:
                    alts.append(alt)
            except:
                continue
    
    def save_story(self, link, profile_name):
        cur_dir = os.getcwd()
        if link[-4:] == ".jpg":
            location = cur_dir + "\\" + "Story" + "\\" + "Images"
            if not os.path.exists(location):
                os.mkdir(location)
            os.chdir(location)
            urllib.request.urlretrieve(link, )
    
    def grab_image(self, profile_name, img_links):
        cur_dir = os.getcwd()
        location = cur_dir + "\\" + profile_name + "\\" + "All images" + "\\" + "Images"
        if not os.path.exists(location):
            os.mkdir(location)
            os.chdir(location)
        counter = 1
        for link in img_links:
            name = str(counter) + ".jpg"
            urllib.request.urlretrieve(link, name)
            counter += 1

class Post():

    def __init__(self, alt, src, likes=None, comments=None):
        self.alt = alt
        self.src = src
        self.comments = comments
        self.likes = likes
        self.comments = comments


class Download():

    def grab_image(self, link):
        pass
        

    def grab_():
        pass
        

def main():
    #account_name, account_password = sys.argv[1:]
    
    
    account = Account(user, password)
    path = "C:\\Users\\George Burac\\Desktop\\chromedriver.exe"
    test = Login(path)
    test.insta_login(account)
  

if __name__ == "__main__":
    main()

