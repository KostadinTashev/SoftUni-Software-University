function deleteByEmail() {
  const input = document.querySelector('input[name="email"]');
  let inputValue = input.value;
  const allEmails = Array.from(document.getElementsByTagName("td"));
  allEmails.forEach((email) => {
    console.log(email === inputValue);
  });
}
