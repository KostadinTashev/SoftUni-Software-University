function sortingNumbers(array) {
  let arr = [];
  sortedArr = array.sort((a, b) => a - b);
  arrayLength = array.length;
  for (let index = 0; index < arrayLength; index++) {
    if (index % 2 === 0) {
      let firstElement = sortedArr.shift();
      arr.push(firstElement);
    } else {
      let lastElement = sortedArr.pop();
      arr.push(lastElement);
    }
  }
  return arr;
}