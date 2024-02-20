function calc() {
  const firstElement = document.getElementById("num1").value;
  const secondElement = document.getElementById("num2").value;
  let sum = Number(firstElement) + Number(secondElement);
  document.getElementById("sum").value = sum;
}
