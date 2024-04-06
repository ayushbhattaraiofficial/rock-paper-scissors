import { Utility } from "./utils.js";
export class RockPaperScissors {
    constructor() {
        this.util = new Utility();
        this.system_choice = this.util.getSystemChoice();
    }

    play() {
        var user_choice = this.util.getUserInput();
        alert(`System ${this.system_choice}, You ${user_choice}`);
        if (this.util.checkWinCondition(user_choice)) {
            return 1;
        } else if (this.util.checkLoseCondition(user_choice)) {
            return 0;
        } else {
            return 2;
        }
    }
}
