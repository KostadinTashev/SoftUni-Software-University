function factorialDivision(firstNum, secondNum) {
  let firstMultiply = 1;
  let secondMultiply = 1;

  for (let index = 1; index <= firstNum; index++) {
    firstMultiply *= index;
  }
  for (let index = 1; index <= secondNum; index++) {
    secondMultiply *= index;
  }

  let result = firstMultiply / secondMultiply;
  console.log(`${result.toFixed(2)}`);
}