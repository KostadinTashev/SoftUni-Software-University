function matrix(number) {
  function printRow(num) {
    let output = "";
    output = `${num} `.repeat(num);
    return output;
  }
  let output = "";
  for (let index = 0; index < number; index++) {
    output += printRow(number) + "\n";
  }
  console.log(output);
}