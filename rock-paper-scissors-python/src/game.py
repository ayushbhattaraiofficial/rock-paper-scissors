from utils import Utility


class RockPaperScissors:
    def __init__(self):
        self.util = Utility()
        self.system_choice = self.util.getSystemChoice()

    def play(self):
        user_choice = self.util.getUserChoice()
        print(f"System: {self.system_choice}, You: {user_choice}")
        if self.util.checkWinCondition(user_choice.upper(), self.system_choice):
            print(f"You Win")
        elif self.util.checkLoseCondition(
            user_choice.upper(), self.system_choice
        ):
            print(f"You Lose")
        else:
            print(f"It's a draw")
