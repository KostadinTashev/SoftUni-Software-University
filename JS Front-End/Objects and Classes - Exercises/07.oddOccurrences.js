function extractOddOccurrences(input) {
  const words = input.toLowerCase().split(" ");
  const wordCount = {};

  words.forEach((word) => {
    if (!wordCount[word]) {
      wordCount[word] = 1;
    } else {
      wordCount[word]++;
    }
  });

  const oddOccurrences = Object.keys(wordCount).filter(
    (word) => wordCount[word] % 2 !== 0
  );

  console.log(oddOccurrences.join(" "));
}