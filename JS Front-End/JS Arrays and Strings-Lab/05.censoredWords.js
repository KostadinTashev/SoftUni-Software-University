function censoredWords(text, word) {
  let censoredText = text.replace(word, "*".repeat(word.length));
  while (censoredText.includes(word)) {
    censoredText = censoredText.replace(word, "*".repeat(word.length));
  }
  console.log(censoredText);
}