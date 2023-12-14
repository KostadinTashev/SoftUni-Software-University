function wordTracker(data) {
  const wordsToFind = data.shift().split(" ");
  const wordCount = new Map(wordsToFind.map((word) => [word, 0]));

  data.forEach((word) => {
    if (wordCount.has(word)) {
      wordCount.set(word, wordCount.get(word) + 1);
    }
  });

  const sortedResult = Array.from(wordCount).sort((a, b) => b[1] - a[1]);

  sortedResult.forEach(([word, count]) => {
    console.log(`${word} - ${count}`);
  });
}