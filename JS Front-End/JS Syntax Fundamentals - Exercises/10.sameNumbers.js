function sameNumbers(number) {
    const numToString = number.toString();
    const firstDigit = numToString[0];
    let sum = 0;
    let allSame = true;
    for (let i = 0; i < numToString.length; i++) {
      sum += Number(numToString[i]);
      if (numToString[i] !== firstDigit) {
        allSame = false;
      }
    }
    console.log(allSame);
    console.log(sum);
  }