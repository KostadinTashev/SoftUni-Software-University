function phoneBook(array) {
  let phoneBookObj = {};
  for (const line of array) {
    let [name, phoneNumber] = line.split(" ");
    phoneBookObj[name] = phoneNumber;
  }
  for (const key in phoneBookObj) {
    console.log(`${key} -> ${phoneBookObj[key]}`);
  }
}