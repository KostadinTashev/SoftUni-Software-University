function pascalCaseSplitter(string) {
  let regex = /[A-Z][a-z]*/gm;
  let matches = string.matchAll(regex);
  let arr = [];

  for (let word of matches) {
    arr.push(word[0]);
  }

  console.log(arr.join(", "));
}