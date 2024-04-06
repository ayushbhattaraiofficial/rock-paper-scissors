from numpy.random import choice


class Utility:
    def __init__(self):
        self.WIN_CONDITIONS = {
            "ROCK": "PAPER",
            "PAPER": "SCISSORS",
            "SCISSORS": "ROCK",
        }
        self.OPTIONS = ["ROCK", "PAPER", "SCISSORS"]

    def getSystemChoice(self):
        return choice(self.OPTIONS)

    def getUserChoice(self):
        while True:
            self.user_choice = str(input("Enter rock, paper or scissor\n"))
            if self.user_choice.upper() in self.OPTIONS:
                return self.user_choice.upper()

    def checkWinCondition(self, user_choice, system_choice):
        return user_choice == self.WIN_CONDITIONS.get(system_choice)

    def checkLoseCondition(self, user_choice, system_choice):
        return system_choice == self.WIN_CONDITIONS.get(user_choice)
