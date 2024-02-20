function subtract() {
  const firstNum = document.getElementById("firstNumber").value;
  const secondNum = document.getElementById("secondNumber").value;
  let subtraction = Number(firstNum) - Number(secondNum);
  const div = document.getElementById("result");
  div.textContent += subtraction;
}
