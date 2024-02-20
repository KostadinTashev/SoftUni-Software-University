function addItem() {
  const listItems = document.getElementById("items");
  const inputField = document.getElementById("newItemText").value;
  const newLi = document.createElement("li");
  newLi.textContent += inputField;
  listItems.appendChild(newLi);
}
