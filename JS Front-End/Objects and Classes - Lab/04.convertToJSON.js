function convertToJson(name, lastName, hairColor) {
  person = {};
  person.name = name;
  person.lastName = lastName;
  person.hairColor = hairColor;
  strJson = JSON.stringify(person);
  console.log(strJson);
}