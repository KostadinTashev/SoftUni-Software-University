function reverseAnArrayOfNumbers(number, array) {
  let reversedArr = array.slice(0, number).reverse().join(" ");
  console.log(reversedArr);
}
