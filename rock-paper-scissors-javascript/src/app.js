import { RockPaperScissors } from "./game.js";

function app() {
    var user_name = prompt("Enter your user name");
    alert(`Welcome to Rock/Paper/Scissors ${user_name}\n Let's play the game`);
    const PLAY = new RockPaperScissors();
    var result = PLAY.play();
    switch (result) {
        case 1:
            alert(`${user_name} wins!!!`);
            break;

        case 0:
            alert(`${user_name} loses!!!`);
            break;
        default:
            alert("It's a draw.");
            break;
    }
}

app();
