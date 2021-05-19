#!/usr/bin/env python3
'''
Whatsapp script
'''

import os
from time import sleep
import logging
from selenium import webdriver, common
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


logging.basicConfig(level=logging.INFO)
logging.info("Starting program")

class Whatsapp:
    '''Web whatsapp setup'''

    def __init__(self):
        '''Publish messages to whatsapp'''
        logging.info('~ __init__()')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.site   = "https://web.whatsapp.com/"
        self.sleep  = 3
        self.base_path = "/home/simon/Documents/projects/Whatsapp/images/{}"

    def open_web_page(self):
        '''Open whatsapp'''
        logging.info('# open_web_page()')
        self.driver.get(self.site)

    def close(self):
        '''Close webpage'''
        sleep(self.sleep)
        open_chat = self.open_chat()
        while not open_chat:
            open_chat = self.open_chat()
        self.send_message('Goodbye')
        self.driver.quit()

    def open_chat(self, name=None):
        '''Go to chat'''
        logging.info('# open_chat()')
        sleep(self.sleep)
        set_chat = False
        if name is None:
            name = 'Yoo-Jin'
        content = '//span[@title="{}"][@dir="auto"]'.format(name)
        try:
            element = self.driver.find_element_by_xpath(content)
            element.click()
            set_chat = True
        except common.exceptions.NoSuchElementException:
            logging.error("Chat group couldn't be found")
        return set_chat

    def send_message(self, message):
        '''Send message in chat'''
        sent = False
        sleep(self.sleep)
        content = '//div[@dir="ltr"][@data-tab="6"][@spellcheck="true"]'
        try:
            element = self.driver.find_element_by_xpath(content)
            element.send_keys(message, Keys.ENTER)
            sent = True
        except common.exceptions.NoSuchElementException:
            logging.error("Message couldn't be sent")
        return sent

    def send_picture(self, picture):
        '''Send picture in chat'''
        attach = '//div[@title = "Attach"]'
        sleep(self.sleep)
        sent = False
        pic = self.base_path.format(picture)
        if not os.path.isfile(pic):
            return sent
        try:
            attachment_section = self.driver.find_element_by_xpath(attach)
            attachment_section.click()
            sleep(self.sleep)
            path = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
            image = self.driver.find_element_by_xpath(path)
            image.send_keys(pic)
            sleep(self.sleep)
            send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            send.click()
            sent = True
        except common.exceptions.NoSuchElementException:
            logging.error("Attachment can't be sent")
        return sent

    def sleep_now(self, sleep_time=None):
        '''Sleep'''
        if sleep_time is None:
            sleep(self.sleep)
        else:
            sleep(sleep_time)
