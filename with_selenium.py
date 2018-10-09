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
    Test = r"https://www.instagram.com/waynerooney"

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
        self.driver.get(Login.Test)
        posts_count = int(str(self.driver.find_element_by_class_name("g47SY ").text))
        print(posts_count)
        profile = self.driver.find_element_by_tag_name("h1").get_attribute("title")
        print(profile)
        img_links = []
        alts = []
        video_links = []

        times_to_scroll = (posts_count // 4)
        scrolls = 0
        while scrolls < times_to_scroll:
            self.driver.execute_script(Login.SCROLL_SCRIPT)
            time.sleep(.2)
            self.get_img_links(img_links)
            self.get_alts(alts)
            self.grab_videos(video_links)
            
            scrolls += 1
        print(len(img_links))
        self.grab_image(profile_name=profile, img_links=img_links)
        #print(len(alts))

    def get_img_mp(self, img_links, likes):
        new_stories = self.driver.find_elements_by_class_name("qFq_l")
        for story in new_stories:
            story.click()
            button_next = self.driver.find_element_by_class_name("  _6CZji")
            while button_next:
                link = self.driver.find_element_by_class("FFVAD").get_attribute("src")
                if link not in img_links:
                    img_links.append(link)
                try:
                    button_next = self.driver.find_element_by_class_name("  _6CZji")
                    try:
                        like = self.driver.find_element_by_class_name("oF4XW sqdOP yWX7d    _8A5w5   ").text
                        likes.append(like)
                    except:
                        print("Likes not found for image at link {}.".format(link))
                        continue
                    button_next.click()
                except:
                    button_next = False
                
    
    def get_story(self):
        profile_pic = self.driver.find_element_by_class_name("_6q-tv").click()
        time.sleep(.2)
        count = len(self.driver.find_elements_by_class_name("_7zQEa"))
        cur_dir = os.getcwd()
        location = cur_dir + "\\" + profile + "\\" + "Story"
        if not os.path.exists(location):
            os.makedirs(location)
            os.chdir(location)
        else:
            os.chdir(location)
        for i in range(count):
            try:
                
                img_link = self.driver.find_element_by_class_name("y-yJ5").get_attribute("src")
                name = str(i) + img_link[-4:]
                if not os.path.exists(os.getcwd() + "\\" + name):
                    print("Downloading {}".format(name))
                    urlretrieve(img_link, name)
                else:
                    print("{} already exists.".format(name))
            except:
                time.sleep(.1)
                img_link = self.driver.find_element_by_class_name("y-yJ5 _7NpAS i1HvM ").get_attribute("src")
                name = str(i) + img_link[-4:]
                if not os.path.exists(os.getcwd() + "\\" + name):
                    print("Downloading {}".format(name))
                    urlretrieve(img_link, name)
                else:
                    print("{} already exists.".format(name))
            try:     
                video_link = self.driver.find_element_by_class_name("y-yJ5  OFkrO ").get_attribute("src")
                name = str(i) + video_link[-4:]
                if not os.path.exists(os.getcwd() + "\\" + name):
                    print("Downloading {}".format(name))
                    urlretrieve(img_link, name)
                else:
                    print("{} already exists.".format(name))
            except:
                time.sleep(.5)
                video_link = self.driver.find_element_by_class_name("y-yJ5  OFkrO ").get_attribute("src")
                name = str(i) + video_link[-4:]
                if not os.path.exists(os.getcwd() + "\\" + name):
                    print("Downloading {}".format(name))
                    urlretrieve(img_link, name)
                else:
                    print("{} already exists.".format(name))
            self.driver.find_element_by_class_name("coreSpriteRightChevron").click()
            time.sleep(.1)
         

    def save_highlights(self,profile):
        cur_dir = os.getcwd()
        location = cur_dir + "\\" + profile + "\\" + "Highlights"
        if not os.path.exists(location):
            os.makedirs(location)
            os.chdir(location)
        else:
            os.chdir(location)
        highlights = self.driver.find_elements_by_class_name("NCYx-")
        for item in highlights:
            item.click()
            count = len(self.driver.find_elements_by_class_name("_7zQEa"))
            for i in range(count):
                link_highlight = self.driver.find_element_by_class_name("y-yJ5 _7NpAS i1HvM ").get_attribute("src")
                urlretrieve(link_highlight, str(i) + link[-4:])
                self.driver.find_element_by_class_name("coreSpriteRightChevron").click()
            time.sleep(.1)
            
        
    def get_likes(self, likes):
        new_posts = self.driver.find_elements_by_class_name("FFVAD")
        for item in new_posts:
            item.click()
            like = self.driver.find_element_by_class_name("oF4XW sqdOP yWX7d    _8A5w5   ")
            like = like.text
            print(like)
            likes.append(like)

    def get_meta_title(self):
        pass

    def get_meta_subject(self):
        pass

    def get_meta_tags(self):
        pass

    def get_meta_comments(self):
        pass
    
    def get_comments(self, comments):
        new_posts = self.driver.find_elements_by_class_name("FFVAD")
        for item in new_posts:
            item.click()
            comment = self.driver.find_elements_by_class("-V_eO")
            print(comment.get_attribute("span"))

    
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
    def get_videos(self, video_links, profile):
        location = os.getcwd() + "\\" + profile + "Videos"
        if not os.path.exists(location):
            os.makedirs(location)
            os.chdir(location)
        else:
            os.chdir(location)
        count = 1
        for link in video_links:
            urlretrieve(link, str(count) + link[-4:])
            count += 1
            
            
                
    
    def get_alts(self, alts):
        new_descriptions = self.driver.find_elements_by_class_name("KL4Bh")
        for desc in new_descriptions:
            try:
                alt = desc.get_attribute("alt")
                if alt not in alts:
                    alts.append(alt)
            except:
                continue
    
    def save_story(self, profile_name):
        cur_dir = os.getcwd()
        self.driver
        if link[-4:] == ".jpg":
            location = cur_dir + "\\" + "Story" + "\\" + "Images"
            if not os.path.exists(location):
                os.makedirs(location)
            os.chdir(location)
            urlretrieve(link, )
    
    def grab_image(self, profile_name, img_links):
        cur_dir = os.getcwd()
        location = cur_dir + "\\" + profile_name + "\\" + "All images" + "\\" + "Images"
        if not os.path.exists(location):
            os.makedirs(location)
            os.chdir(location)
        else:
            os.chdir(location)
        counter = 1
        for link in img_links:
            name = str(counter) + ".jpg"
            if not os.path.exists(os.getcwd() + "\\" + name):
                print("Downloading image {}".format(name))        
                urlretrieve(link, name)
            else:
                print("The file {} already exists.".format(name))
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

    #targets = [i for i in open(sys.argv[1], "r").readlines()]
    #users = [Account(I, P) for I, P in open(sys.argv[2], "r").readline()]

  

if __name__ == "__main__":
    main()

