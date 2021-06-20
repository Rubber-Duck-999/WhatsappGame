#!/usr/bin/env python3
'''
People script
'''

import logging
import random

logging.basicConfig(level=logging.INFO)
logging.info("Starting program")

class People:
    '''People and rounds setup'''

    def __init__(self):
        '''Constructor'''
        logging.info('~ __init__()')
        self.people = [
            {
                "name": "Dad",
                "guess": False,
            },
            {
                "name": "Mum",
                "guess": False,
            },
            {
                "name": "Yoo-Jin",
                "guess": False,
            },
            {
                "name": "Yoo-Jin",
                "guess": False,
            }
        ]

    def get_number(self):
        '''Random number'''
        max = len(self.people) - 1
        num = random.randint(0, max)
        return num

    def get_person(self):
        loop = True
        name = self.people[0]['name']
        while loop:
            num = self.get_number()
            if self.people[num]["guess"] is False:
                self.people[num]["guess"] = True
                name = self.people[num]["name"]
                loop = False
        return name
