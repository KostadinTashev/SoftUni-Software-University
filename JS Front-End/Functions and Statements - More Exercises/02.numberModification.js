function numberModification(number) {
  let sum = 0;
  let numberAsString = String(number);
  let arr = [];

  for (let index = 0; index < numberAsString.length; index++) {
    let currentNum = Number(numberAsString[index]);
    sum += currentNum;
    arr.push(currentNum);
  }

  let average = sum / numberAsString.length;
  while (average < 5) {
    arr.push(9);
    sum += 9;
    average = sum / arr.length;
  }

  console.log(parseInt(arr.join("")));
}