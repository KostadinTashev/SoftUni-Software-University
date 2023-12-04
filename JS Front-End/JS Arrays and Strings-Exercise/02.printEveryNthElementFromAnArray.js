function printEveryNthElementFromAnArray(array, number) {
  let newArr = [];
  for (let index = 0; index < array.length; index += number) {
    newArr.push(array[index]);
  }
  return newArr;
}
