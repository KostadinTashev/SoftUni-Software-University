function arrayRotation(array, numberOfRotation) {
  for (let index = 0; index < numberOfRotation; index++) {
    let element = array.shift();
    array.push(element);
  }
  console.log(array.join(" "));
}
