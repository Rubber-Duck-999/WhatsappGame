#!/usr/bin/env python3
'''
Whatsapp script
'''

from selenium import webdriver
from selenium import common
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting program")

class Whatsapp:
    '''Web whatsapp setup'''

    def __init__(self):
        '''Publish messages to whatsapp'''
        logging.info('~ __init__()')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.site   = "https://web.whatsapp.com/"
        self.sleep  = 5

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
        set = False
        if name == None:
            name = 'Yoo-Jin'
        content = '//span[@title="{}"][@dir="auto"]'.format(name)
        try:
            element = self.driver.find_element_by_xpath(content)
            element.click()
            set = True
        except common.exceptions.NoSuchElementException:
            logging.error("Chat group couldn't be found")
        return set

    def send_message(self, message):
        '''Send message in chat'''
        sent = False
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
        if not os.path.isfile(picture):
           return 
        try:
            attachment_section = self.driver.find_element_by_xpath(attach)
            attachment_section.click()
            sleep(self.sleep)
            path = '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
            image = self.driver.find_element_by_xpath(path)
            image.send_keys(picture)
            sleep(self.sleep)
            send = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            send.click()
        except common.exceptions.NoSuchElementException:
            logging.error("Attachment can't be sent")

    def run_game(self):
        '''Set up and play'''
        try:
            self.open_web_page()
            sleep(self.sleep)
            chat_open = self.open_chat()
            while not chat_open:
                sleep(self.sleep)
                chat_open = self.open_chat()
            self.send_message('Kiss me')
            self.send_picture(self.files[0])
            self.close()
        except KeyboardInterrupt:
            logging.error('Leave')

game = Whatsapp()
game.run_game()