function passwordValidator(password) {
  function validLength(text) {
    return text.length >= 6 && text.length <= 10;
  }

  function isAlphanumeric(text) {
    const regex = /^[a-zA-Z0-9]+$/;
    return regex.test(text);
  }

  function digitsCount(text) {
    let digits = 0;
    for (let index = 0; index < text.length; index++) {
      if (!isNaN(parseInt(text[index]))) {
        digits += 1;
      }
    }
    return digits >= 2;
  }

  if (!validLength(password)) {
    console.log("Password must be between 6 and 10 characters");
  }
  if (!isAlphanumeric(password)) {
    console.log("Password must consist only of letters and digits");
  }
  if (!digitsCount(password)) {
    console.log("Password must have at least 2 digits");
  }

  if (
    validLength(password) &&
    isAlphanumeric(password) &&
    digitsCount(password)
  ) {
    console.log("Password is valid");
  }
}