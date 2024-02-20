function editElement(element, match, replacer) {
  if (element && element.textContent) {
    element.textContent = element.textContent.replace(new RegExp(match, 'g'), replacer);
  }
}