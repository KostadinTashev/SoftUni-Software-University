function solve() {
  let input = document.getElementById('input').value;
  let output = document.getElementById('output');

  output.innerHTML = "";

  let arrayText = input.split(".");


  for(let i = 0; i < arrayText.length;i+=3){
    let res = [];

    for(let x = 0; x < 3;x++){
      if(arrayText[i+x]){
        res.push(arrayText[i+x]);
      }
    }

    let textRes = res.join('. ') + '.'.trim();

  output.innerHTML += `<p>${textRes}</p>`
  }

  let textRes = res.join('. ') + '.'

  output.innerHTML += `<p>${textRes}</p>`
}