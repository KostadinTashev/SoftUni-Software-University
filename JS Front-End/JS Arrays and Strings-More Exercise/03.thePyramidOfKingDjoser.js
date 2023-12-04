function thePyramidOfKingDjoser(base, increment) {
  let stones = 0;
  let marbles = 0;
  let lapis = 0;
  let gold = 0;
  let steps = 0;
  while (base > 0) {
    steps++;
    if (base === 1 || base === 2) {
      gold += base * base * increment;
      break;
    }
    if (steps % 5 == 0) {
      lapis += (base * base - (base - 2) ** 2) * increment;
      stones += (base - 2) ** 2 * increment;
    } else {
      stones += (base - 2) ** 2 * increment;
      marbles += (base * base - (base - 2) ** 2) * increment;
    }
    base -= 2;
  }
  console.log(`Stone required: ${Math.ceil(stones)}`);
  console.log(`Marble required: ${Math.ceil(marbles)}`);
  console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
  console.log(`Gold required: ${Math.ceil(gold)}`);
  let height = Math.floor(steps * increment);
  console.log(`Final pyramid height: ${height}`);
}
