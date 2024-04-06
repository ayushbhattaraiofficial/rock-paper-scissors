export class Utility {
    constructor() {
        this.OPTIONS = ["ROCK", "PAPER", "SCISSORS"];
        this.WIN_CONDITIONS = {
            ROCK: "PAPER",
            PAPER: "SCISSORS",
            SCISSORS: "ROCK",
        };
    }

    getSystemChoice() {
        var choice_index = Math.floor(Math.random() * this.OPTIONS.length);
        this.system_choice = this.OPTIONS[choice_index];
        return this.system_choice;
    }
    getUserInput() {
        while (true) {
            var user_choice = prompt("Enter rock, paper or scissors");
            if (this.OPTIONS.includes(user_choice.toUpperCase())) {
                return user_choice.toUpperCase();
            } else {
                alert("The choice is incorrect");
            }
        }
    }

    checkWinCondition(user_choice) {
        return user_choice === this.WIN_CONDITIONS[this.system_choice];
    }

    checkLoseCondition(user_choice) {
        return this.system_choice === this.WIN_CONDITIONS[user_choice];
    }
}
