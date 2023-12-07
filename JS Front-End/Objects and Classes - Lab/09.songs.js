function songInfo(array) {
  class Song {
    constructor(type, name, time) {
      this.type = type;
      this.name = name;
      this.time = time;
    }
  }

  let songs = [];
  let numberOfSongs = array.shift();
  let typeSong = array.pop();

  for (let i = 0; i < numberOfSongs; i++) {
    let [type, name, time] = array[i].split("_");
    let song = new Song(type, name, time);
    songs.push(song);
  }

  if (typeSong === "all") {
    songs.forEach((song) => console.log(song.name));
  } else {
    let filtered = songs.filter((song) => song.type === typeSong);
    filtered.forEach((song) => console.log(song.name));
  }
}