function charactersInRange(charOne, charTwo) {
  let output = ''
  let charOneToInt = charOne.charCodeAt();
  let charTwoToInt = charTwo.charCodeAt();
  let start = Math.min(charOneToInt, charTwoToInt);
  let end = Math.max(charOneToInt, charTwoToInt);
  for (let index = start + 1; index < end; index++) {
    element = String.fromCharCode(index);
    output += element + ' '
  }
  console.log(output);
}