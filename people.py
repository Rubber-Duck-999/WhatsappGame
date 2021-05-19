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
                "name": "Phil Gladwell",
                "guess": True,
            },
            {
                "name": "Sammi",
                "guess": True,
            },
            {
                "name": "Liz",
                "guess": True,
            },
            {
                "name": "Michelle",
                "guess": True,
            },
            {
                "name": "Rich",
                "guess": True,
            },
            {
                "name": "Yoo-Jin",
                "guess": False,
            },
            {
                "name": "Clare",
                "guess": True,
            },
            {
                "name": "Simon",
                "guess": True,
            },
            {
                "name": "Becky",
                "guess": True,
            },
            {
                "name": "Dale",
                "guess": True,
            }
        ]
        self.group = "Alpha"

    def get_number(self):
        '''Random number'''
        max = len(self.people) - 1
        num = random.randint(0, max)
        return num

    def get_person(self):
        name = self.people[5]["name"]
        for person in range(len(self.people)):
            num = self.get_number()
            if self.people[num]["guess"] is False:
                #self.people[num]["guess"] = True
                name = self.people[num]["name"]
        return name


class Guess:

    def __init__(self):
        '''Constructor'''
        self.guesses = [
            {
                "file": "cheese.jpeg",
                "name": "Double Gloucester Cheese",
                "done": False
            },
            {
                "file": "ducks.jpg",
                "name": "Rubber Ducks",
                "done": False
            },
            {
                "file": "chicken.jpeg",
                "name": "Live Chicken",
                "done": False
            },
            {
                "file": "porsche.jpg",
                "name": "Porsche Sports Car",
                "done": False
            },
            {
                "file": "south_africa_map.jpg",
                "name": "South Africa",
                "done": False
            },
        ]
        self.title = 'Game of Guesses - (Yes or No)'
        self.description = "This is the game of guessing yes or no from a another person's image, they cannot describe it. Only yes or no to questions from other users"

    def get_number(self):
        '''Random number'''
        max = len(self.guesses) - 1
        num = random.randint(0, max)
        return num

    def get_guess(self):
        for person in range(len(self.guesses)):
            num = self.get_number()
            if self.guesses[num]["done"] is False:
                self.guesses[num]["done"] = True
                return self.guesses[num]
        return self.guesses[0]
