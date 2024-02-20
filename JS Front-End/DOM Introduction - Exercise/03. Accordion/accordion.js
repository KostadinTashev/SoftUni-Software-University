function toggle() {
  const button = document.getElementsByClassName("button")[0];
  const textToDisplay = document.getElementById("extra");
    if(button.textContent === "More"){
        textToDisplay.style.display = "block";
        button.textContent = 'Less'
    }else{
        textToDisplay.style.display = 'none';
        button.textContent = 'More'
    }
}
