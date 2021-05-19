#!/usr/bin/env python3
'''
People script
'''

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting program")

class People:
    '''People and rounds setup'''

    def __init__(self):
        '''Constructor'''
        logging.info('~ __init__()')
        self.people = [
            "Sammi",
            "Phil",
            "Liz",
            "Michelle",
            "Rich",
            "Yoo-Jin",
            "Clare",
            "Simon",
            "Becky",
            "Dale"
        ]
        self.group = "Alpha"

class Guess:

    def __init__(self):
        '''Constructor'''
        self.base_path = "/home/simon/Documents/projects/Whatsapp/images/{}"
        self.files = [
            {
                "file": "cheese.jpeg",
                "name": "Double Gloucester Cheese"
            },
            {
                "file": "ducks.jpeg",
                "name": "Rubber Ducks"
            },
            {
                "file": "chicken.jpg",
                "name": "Live Chicken"
            },
            {
                "file": "porsche.jpg",
                "name": "Porsche Sports Car"
            },
            {
                "file": "south_africa_map.jpg",
                "name": "South Africa"
            },
        ]

class Idioms:

    def __init__(self):
        self.guesses = [
            {
                "anagram": "A gentleman",
                "word": "Elegant Man"
            },
            {
                "anagram": "Lardy Mango",
                "word": "Gary Oldman"
            },
            {
                "anagram": "Cash lost in me",
                "word": "Slot Machine"
            }
        ]