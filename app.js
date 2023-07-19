// Init score and Score Display
let ScoreDisp = document.getElementById('ScoreDisp');
let score = 0;

// Add event listener to the click button
document.querySelector('button').addEventListener("click", click);

// The function the button executes on click
function click(){
    ScoreDisp.class = "text-bold text-center text-8xl md:text-9xl m-9 dark:text-white";
    score += 1;
    ScoreDisp.innerHTML = score;
    if( score == 100 ){
        ScoreDisp.class += "transition-all duration-150 rotate-[360deg]";
    }
}
