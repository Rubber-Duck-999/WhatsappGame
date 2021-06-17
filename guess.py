class Guess:

    def __init__(self):
        '''Constructor'''
        self.words = [
            "",
            ""
        ]
        self.guesses = [
            {
                "file": "",
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