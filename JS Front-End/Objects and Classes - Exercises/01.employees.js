function employees(listOfEmployees) {
  listOfEmployees.forEach((element) => {
    console.log(`Name: ${element} -- Personal Number: ${element.length}`);
  });
}