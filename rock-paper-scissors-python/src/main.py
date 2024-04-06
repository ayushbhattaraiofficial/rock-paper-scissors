from game import RockPaperScissors


def main():
    user_name = str(input("Please enter your username\n"))
    print(f"Welcome to the game {user_name}")
    print(f"Let's Play!")
    play_now = RockPaperScissors()
    play_now.play()


if __name__ == "__main__":
    main()
