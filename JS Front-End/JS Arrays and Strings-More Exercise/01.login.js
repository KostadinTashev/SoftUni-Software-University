function login(arrayOfStrings) {
  let username = arrayOfStrings.shift();
  let counter = 0;
  for (word of arrayOfStrings) {
    counter++;
    if (username.split("").reverse().join("") === word) {
      console.log(`User ${username} logged in.`);
    } else {
      if (counter === 4) {
        console.log(`User ${username} blocked!`);
        break;
      }
      console.log("Incorrect password. Try again.");
    }
  }
}