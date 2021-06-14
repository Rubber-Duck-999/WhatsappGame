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
                "name": "Kim",
                "guess": False,
            },
            {
                "name": "Ola",
                "guess": False,
            },
            {
                "name": "Yoo-Jin",
                "guess": False,
            },
            {
                "name": "Thirza",
                "guess": False,
            },
            {
                "name": "Ola",
                "guess": False,
            },
            {
                "name": "Derek",
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


class Guess:

    def __init__(self):
        '''Constructor'''
        self.guesses = [
            {
                "file": "yorkshire_wensleydale.jpg",
                "name": "Wensleydale Cheese",
                "done": False
            },
            {
                "file": "peppa_pig.jpeg",
                "name": "Peppa Pig",
                "done": False
            },
            {
                "file": "ferrari.jpg",
                "name": "Ferrari Sports Car",
                "done": False
            },
            {
                "file": "botswana_map.jpg",
                "name": "Botswana",
                "done": False
            },
            {
                "file": "clover.png",
                "name": "Clover Leaf",
                "done": False
            },
            {
                "file": "airplane.jpg",
                "name": "Airplane",
                "done": False
            }
        ]
        self.title = 'Guess the Picture - (Yes or No)'
        self.description = "This is the game of guessing yes or no from a another person's picture, they cannot describe it. Only yes or no to questions from other users"

    def get_number(self):
        '''Random number'''
        max = len(self.guesses) - 1
        num = random.randint(0, max)
        return num

    def get_guess(self):
        for index in range(len(self.guesses)):
            num = self.get_number()
            if self.guesses[num]["done"] is False:
                self.guesses[num]["done"] = True
                return self.guesses[num]
        return self.guesses[0]
