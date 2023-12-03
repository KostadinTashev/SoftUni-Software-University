function evenAndOddSubtraction(array) {
  let EvenSum = 0;
  let OddSum = 0;
  for (const num of array) {
    let isEven = num % 2 === 0;
    if (isEven) {
      EvenSum += num;
    } else {
      OddSum += num;
    }
  }
  let result = EvenSum - OddSum;
  console.log(result);
}

