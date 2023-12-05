function carWash(commands) {
  let clean = 0;
  for (const command of commands) {
    if (command === "soap") {
      clean += 10;
    } else if (command === "water") {
      clean *= 1.2;
    } else if (command === "vacuum cleaner") {
      clean *= 1.25;
    } else if (command === "mud") {
      clean *= 0.9;
    }
  }
  console.log(`The car is ${clean.toFixed(2)}% clean.`);
}