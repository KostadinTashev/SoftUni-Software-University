function oddAndEvenSum(number) {
  let numberAsString = String(number);
  let oddSum = 0;
  let evenSum = 0;
  for (let index = 0; index < numberAsString.length; index++) {
    let currentNum = Number(numberAsString[index]);
    if (currentNum % 2 === 0) {
      evenSum += currentNum;
    } else {
      oddSum += currentNum;
    }
  }
  console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}