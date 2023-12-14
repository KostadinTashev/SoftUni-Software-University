function storeProvision(currentStock, orderedProducts) {
  const stock = {};

  for (let i = 0; i < currentStock.length; i += 2) {
    const product = currentStock[i];
    const quantity = parseInt(currentStock[i + 1]);

    stock[product] = quantity;
  }
  for (let i = 0; i < orderedProducts.length; i += 2) {
    const product = orderedProducts[i];
    const quantity = parseInt(orderedProducts[i + 1]);
    if (stock[product]) {
      stock[product] += quantity;
    } else {
      stock[product] = quantity;
    }
  }
  for (const product in stock) {
    console.log(`${product} -> ${stock[product]}`);
  }
}