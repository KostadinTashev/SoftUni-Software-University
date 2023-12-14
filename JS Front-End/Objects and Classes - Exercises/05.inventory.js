function inventory(input) {
    const heroes = input.map((line) => {
      const [hero, level, items] = line.split(" / ");
      return {
        hero,
        level: Number(level),
        items: items.split(", "),
      };
    });
  
    const sortedHeroes = heroes.sort((heroA, heroB) => heroA.level - heroB.level);
  
    for (const { hero, level, items } of sortedHeroes) {
      console.log(`Hero: ${hero}`);
      console.log(`level => ${level}`);
      console.log(`items => ${items.join(", ")}`);
    }
  }