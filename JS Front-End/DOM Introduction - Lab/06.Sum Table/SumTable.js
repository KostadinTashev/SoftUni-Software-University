function sumTable() {
  const costs = Array.from(
    document.querySelectorAll("table tbody tr td:last-child")
  );
  let total = 0;
  for (let index = 0; index < costs.length - 1; index++) {
    let cost = parseFloat(costs[index].textContent);
    if (!isNaN(cost)) {
      total += cost;
    }
  }
  document.getElementById("sum").textContent = total.toFixed(2);
}
