function printHelix(length) {
  let sequence = "ATCGTTAGGG";
  let index = 0;

  for (let i = 0; i < length; i++) {
    let line = "";

    if (i % 4 === 0) {
      line += `**${sequence[index]}${sequence[index + 1]}**`;
      index += 2;
    } else if ((i - 1) % 4 === 0) {
      line += `*${sequence[index]}--${sequence[index + 1]}*`;
      index += 2;
    } else if ((i - 2) % 4 === 0) {
      line += `${sequence[index]}----${sequence[index + 1]}`;
      index += 2;
    } else if ((i - 3) % 4 === 0) {
      line += `*${sequence[index]}--${sequence[index + 1]}*`;
      index += 2;
    }

    console.log(line);
    if (index >= sequence.length) {
      index = 0;
    }
  }
}