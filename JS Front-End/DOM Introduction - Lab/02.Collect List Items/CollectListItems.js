function extractText() {
  const listItems = Array.from(document.querySelectorAll("ul > li"));
  const area = document.getElementById("result");
  for (const list of listItems) {
    area.value += list.textContent + "\n";
  }
}
