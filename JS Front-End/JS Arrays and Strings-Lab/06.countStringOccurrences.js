function countStringOccurrences(text, word) {
  let words = text.split(" ");
  let counter = 0;
  for (const currWord of words) {
    if (currWord === word) {
      counter += 1;
    }
  }
  console.log(counter);
}