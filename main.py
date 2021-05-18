#!/usr/bin/env python3
'''
Whatsapp script
'''

from selenium import webdriver
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
        self.sleep  = 30
        self.user   = 'Yoo-Jin'
        self.files  = ["images/cheese.jpeg"]

    def open_web_page(self):
        '''Open whatsapp'''
        logging.info('# open_web_page()')
        self.driver.get(self.site)

    def open_chat(self):
        '''Go to chat'''
        logging.info('# open_chat()')
        set = False
        content = '//span[@title="{}"][@dir="auto"]'.format(self.user)
        element = self.driver.find_element_by_xpath(content)
        if len(element) > 0:
            element.click()
            set = True
        else:
            logging.error("Chat group couldn't be found")
        return set

    def send_message(self, message):
        '''Send message in chat'''
        sent = False
        content = '//div[@dir="ltr"][@data-tab="6"][@spellcheck="true"]'
        element = self.driver.find_element_by_xpath(content)
        if len(element) > 0:
            element.send_keys(message, Keys.ENTER)
            sent = True
        else:
            logging.error("Message couldn't be sent")
        return sent

    def run_game(self):
        '''Set up and play'''
        self.open_web_page()

game = Whatsapp()
game.run_game()