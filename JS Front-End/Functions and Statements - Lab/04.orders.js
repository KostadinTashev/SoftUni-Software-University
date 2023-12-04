function orders(product, quantity) {
  let coffeePrice = 1.5;
  let waterPrice = 1;
  let cokePrice = 1.4;
  let snacksPrice = 2.0;
  let totalPrice = 0;
  if (product === "coffee") {
    totalPrice = coffeePrice * quantity;
  } else if (product === "water") {
    totalPrice = waterPrice * quantity;
  } else if (product === "coke") {
    totalPrice = cokePrice * quantity;
  } else {
    totalPrice = snacksPrice * quantity;
  }
  console.log(totalPrice.toFixed(2));
}