function signCheck(numOne, numTwo, numThree) {
  let countNegativeeNumbers = 0;
  if (numOne < 0) {
    countNegativeeNumbers += 1;
  }
  if (numTwo < 0) {
    countNegativeeNumbers += 1;
  }
  if (numThree < 0) {
    countNegativeeNumbers += 1;
  }
  if (countNegativeeNumbers % 2 == 0) {
    console.log("Positive");
  } else {
    console.log("Negative");
  }
}
signCheck(-6, -12, 14);
