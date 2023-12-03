function sumFirstAndLastArrayElements(arr) {
  //First way
  let firstEl = arr.shift();
  let lastEl = arr.pop();
  let result = firstEl + lastEl;
  console.log(result);
  //Second way
  //   let firstEl = arr[0];
  //   let lastEl = arr[arr.length - 1];
  //   let result = firstEl + lastEl;
  //   console.log(result);
}

