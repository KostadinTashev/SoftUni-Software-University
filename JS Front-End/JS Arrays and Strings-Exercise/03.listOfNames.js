function listOfNames(names) {
  names.sort((a, b) => a.localeCompare(b));
  index = 1;
  for (const name of names) {
    console.log(`${index}.${name}`);
    index++;
  }
}