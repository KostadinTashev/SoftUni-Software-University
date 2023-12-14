function combineTermsAndDefinitions(input) {
  const dictionary = {};

  input.forEach((str) => {
    const obj = JSON.parse(str);
    Object.entries(obj).forEach(([term, definition]) => {
      dictionary[term] = definition;
    });
  });

  const sortedTerms = Object.keys(dictionary).sort();

  sortedTerms.forEach((term) => {
    console.log(`Term: ${term} => Definition: ${dictionary[term]}`);
  });
}
