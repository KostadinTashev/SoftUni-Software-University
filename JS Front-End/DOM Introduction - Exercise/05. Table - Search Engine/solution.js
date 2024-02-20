function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);
  const ElementTh = Array.from(document.getElementsByTagName("td"));
  function onClick() {
  const result = document.getElementById("searchField").value;
    for (const element of ElementTh) {
      if (element.textContent.includes(result)) {
        element.parentElement.classList.add('select');
      }
    }
    document.getElementById("searchField").value = '';
  }
}
