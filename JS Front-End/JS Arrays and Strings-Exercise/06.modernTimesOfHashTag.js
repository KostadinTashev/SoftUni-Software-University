function modernTimes(sentence) {
  let regex = /#[A-Za-z]+/gm;
  let matches = sentence.match(regex);
  for (const match of matches) {
    console.log(match.slice(1));
  }
}