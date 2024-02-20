function solve() {
  const text = document.getElementById("text").value;
  const currentCase = document.getElementById("naming-convention").value;
  let textArray = text.split(' ');
  let result = '';

  switch (currentCase) {
    case "Camel Case":
      textArray.forEach((e,i)=>{
        if(i === 0){
          return result += e.toLowerCase();
        }
        return result+= e[0].toUpperCase() + e.substring(1).toLowerCase();

        
      })
      break;

    case "Pascal Case":

    textArray.forEach((e,i)=>{
      e = e.toLowerCase();
      result += e[0].toUpperCase() + e.substring(1);
    })
      break;

    default:
      result = "Error!";
  }

  document.getElementById("result").textContent = result;
}
