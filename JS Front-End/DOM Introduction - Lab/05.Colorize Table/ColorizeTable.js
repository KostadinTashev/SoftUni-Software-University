function colorize() {
  const row = Array.from(document.getElementsByTagName("tr"));
  for (let index = 1; index < row.length; index += 2) {
    row[index].style.background = "Teal";
  }
}
