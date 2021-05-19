#!/usr/bin/env python3
'''
Whatsapp script
'''

import logging
import whatsapp
import people

logging.basicConfig(level=logging.INFO)
logging.info("Starting program")

class Game:
    '''Game setup'''

    def __init__(self):
        '''Publish messages to whatsapp'''
        logging.info('__init__()')
        self.app    = whatsapp.Whatsapp()
        self.people = people.People()
        self.guess  = people.Guess()
        self.current_person = 'Yoo-Jin'
        self.group_name     = 'Phil Gladwell'

    def tell_group(self, title, description):
        '''Tell each group game name
        and rules'''
        if self.group_name not in self.current_person:
            chat_open = self.app.open_chat(self.group_name)
            while not chat_open:
                chat_open = self.app.open_chat(self.group_name)
            self.current_person = self.group_name
        self.app.send_message(title)
        self.app.send_message(description)

    def play_guesses(self):
        '''Play this game'''
        logging.info('Lets start')
        self.tell_group(self.guess.title, self.guess.description)
        done = False
        round = 1
        while not done and round < 6:
            person_name = self.people.get_person()
            message = 'Round {}'.format(str(round), person_name)
            self.tell_group(message, person_name)
            if person_name not in self.current_person:
                while not self.app.open_chat(person_name):
                    logging.error("Can't send message")
                    self.app.sleep_now()
            self.current_person = person_name
            guess = self.guess.get_guess()
            self.app.send_picture(guess['file'])
            self.app.send_message(guess['name'])
            round += 1
            wait = input('Wait for next round, enter')
            #self.tell_group('Answer', guess['name'])
            logging.info('Finished round')
        self.choose_game()

    def choose_game(self):
        '''Choose game to play'''
        logging.info('Enter your game of choice:')
        logging.info('1: Guesses')
        choice = input()
        if choice == '1':
            self.play_guesses()
        elif choice == 'exit':
            logging.info('Returning')
        else:
            logging.error('Please input a correct choice')
            self.choose_game()

    def run_game(self):
        '''Set up and play'''
        try:
            chat_open = self.app.open_chat()
            if not chat_open:
                chat_open = self.app.open_chat()
                self.run_game()
            self.current_person = self.people.group
            self.choose_game()
        except KeyboardInterrupt:
            logging.error('Leave')
        except ConnectionRefusedError:
            logging.error('Going....')
        self.app.close()

    def start(self):
        self.app.open_web_page()
        self.run_game()

game = Game()
game.start()
