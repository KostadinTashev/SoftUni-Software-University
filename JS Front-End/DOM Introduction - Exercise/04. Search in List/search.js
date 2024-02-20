function search() {
  const search = document.getElementById("searchText").value.toLowerCase();
  let matches = 0;
  const liItems = Array.from(document.getElementById("towns").children);

  for (const li of liItems) {
    li.style.fontWeight = "normal";
    li.style.textDecoration = "none"; 

    if (li.textContent.toLowerCase().includes(search)) {
      matches += 1;
      li.style.fontWeight = "bold"; 
      li.style.textDecoration = "underline"; 
    }
  }
  document.getElementById("result").textContent = `${matches} matches found`;
}
