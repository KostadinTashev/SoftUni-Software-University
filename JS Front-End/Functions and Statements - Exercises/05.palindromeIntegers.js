function palindromeIntegers(arr) {
  for (const number of arr) {
    currentNum = String(number);
    reversedNum = currentNum.split("").reverse().join("");
    console.log(currentNum === reversedNum);
  }
}