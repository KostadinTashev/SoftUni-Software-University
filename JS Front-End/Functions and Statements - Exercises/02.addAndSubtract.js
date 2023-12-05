function addAndSubtract(numOne, numTwo, numThree) {
  function sum(numOne, numTwo) {
    return numOne + numTwo;
  }
  function subtract(result, numThree) {
    return result - numThree;
  }
  let sumResult = sum(numOne, numTwo);
  let finalResult = subtract(sumResult, numThree);
  console.log(finalResult);
}