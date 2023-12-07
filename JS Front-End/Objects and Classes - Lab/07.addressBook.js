function storeInfo(info) {
  const addressBook = {};

  for (let i = 0; i < info.length; i++) {
    const [name, address] = info[i].split(":");
    addressBook[name] = address;
  }

  const sortedNames = Object.keys(addressBook).sort();

  for (let j = 0; j < sortedNames.length; j++) {
    const name = sortedNames[j];
    console.log(`${name} -> ${addressBook[name]}`);
  }
}