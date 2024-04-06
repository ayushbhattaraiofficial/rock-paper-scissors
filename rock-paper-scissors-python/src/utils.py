from numpy.random import choice


class Utility:
    def __init__(self):
        self.win_conditions = {
            "ROCK": "PAPER",
            "PAPER": "SCISSORS",
            "SCISSORS": "ROCK",
        }
        self.options = ["ROCK", "PAPER", "SCISSORS"]

    def getSystemChoice(self):
        return choice(self.options)

    def getUserChoice(self):
        while True:
            self.user_choice = str(input("Enter rock, paper or scissor\n"))
            if self.user_choice.upper() in self.options:
                return self.user_choice.upper()

    def checkWinCondition(self, user_choice, system_choice):
        return user_choice == self.win_conditions.get(system_choice)

    def checkLoseCondition(self, user_choice, system_choice):
        return system_choice == self.win_conditions.get(user_choice)
