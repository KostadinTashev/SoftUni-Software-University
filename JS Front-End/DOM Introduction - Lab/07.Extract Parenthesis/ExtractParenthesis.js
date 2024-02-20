function extract(content) {
  const targetElement = document.getElementById(content);
  if (targetElement) {
    const text = targetElement.textContent;
    const regex = /\(([^)]+)\)/g;
    const matches = text.match(regex);

    if (matches) {
      return matches.join("; ");
    } else {
      return "No parenthesized text found.";
    }
  } else {
    return "Element not found.";
  }
}
