from selenium import webdriver
from PIL import Image
import time
import sys
import os
import urllib
import cStringIO


class Chat(object):

    def __init__(self, url):
        self.chrome = webdriver.Chrome()
        self.chrome.get(url)
        return

    def get_wechat_img(self):
        login_button = self.chrome.find_element_by_id('loginBtn')
        login_button.click()
        self.chrome.switch_to.frame(0)
        wechat_img = self.chrome.find_element_by_css_selector('img').get_property('src')
        self.chrome.switch_to.default_content()
        return wechat_img

    def print_image(self, url):
        img_file = cStringIO.StringIO(urllib.urlopen(url).read())
        img = Image.open(img_file)
        img.show()
        return True

    def is_login(self):
        login_button = self.chrome.find_element_by_id('loginBtn')

        if login_button != 1:
            self.chrome.close()
            self.__init__()
            return None

        return None

    def get_text(self):

        ac = self.chrome.find_element_by_id("loader")
        style = ac.get_attribute("style")
        while style != "display: none;":
            self.chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            ac = self.chrome.find_element_by_id("loader")
            style = ac.get_attribute("style")
        el = self.chrome.find_elements_by_xpath('//div[@class="mazi-activity-container item-container"]/div[@class="col-md-12"]')
        href_list = []
        for e in el:
            et = e.find_element_by_xpath("./a")
            href = et.get_attribute("href")
            et = e.find_element_by_xpath('.//a[@class="textTag category"]')
            catalog = et.get_attribute("innerHTML")
            et = e.find_element_by_xpath('.//div[@class="item-titleV2"]')
            title = et.get_attribute("innerHTML")
            et = e.find_element_by_xpath('.//div[@class="item-author-nameV2"]')
            author = et.get_attribute("innerHTML")
            et = e.find_element_by_xpath('.//span[@class="text"]')
            readers = et.get_attribute("innerHTML")

            href_list.append(href)

        print (href_list)


pass


target = 'http://gitbook.cn/gitchat/hot'

chat = Chat(target)

wechatImg = chat.get_wechat_img()

chat.print_image(wechatImg)

time.sleep(10)

chat.get_text()

