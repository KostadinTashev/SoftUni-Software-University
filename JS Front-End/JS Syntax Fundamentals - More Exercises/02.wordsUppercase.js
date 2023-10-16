function wordsUppercase(text) {
    let expression = text.matchAll(/\w+/gm);
    let result = [];
    for (array of expression) {
      result.push(array[0].toUpperCase());
    }
    console.log(result.join(", "));
}  