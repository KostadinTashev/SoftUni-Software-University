function towns(cities) {
  let townObjects = [];

  for (const currCity of cities) {
    let [town, latitude, longitude] = currCity.split(" | ");

    let formattedTown = {
      town: town,
      latitude: Number(latitude).toFixed(2),
      longitude: Number(longitude).toFixed(2),
    };

    console.log(formattedTown);
  }
}