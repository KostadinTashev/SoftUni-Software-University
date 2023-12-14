function movies(input) {
  const moviesList = [];

  for (const line of input) {
    if (line.includes("addMovie")) {
      const nameOfMovie = line.split("addMovie ")[1];
      moviesList.push({ name: nameOfMovie });
    } else if (line.includes("directedBy")) {
      const [name, director] = line.split(" directedBy ");
      const movie = moviesList.find(
        (movieObj) => movieObj.name === name.trim()
      );
      if (movie) {
        movie.director = director;
      }
    } else if (line.includes("onDate")) {
      const [name, date] = line.split(" onDate ");
      const movie = moviesList.find(
        (movieObj) => movieObj.name === name.trim()
      );
      if (movie) {
        movie.date = date;
      }
    }
  }

  const moviesWithInfo = moviesList.filter(
    (movie) => movie.name && movie.director && movie.date
  );
  moviesWithInfo.forEach((movie) => console.log(JSON.stringify(movie)));
}
