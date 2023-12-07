function catInfo(array) {
  let cats = [];

  class Cat {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }

    meow() {
      console.log(`${this.name}, age ${this.age} says Meow`);
    }
  }

  for (let i = 0; i < array.length; i++) {
    let catData = array[i].split(" ");
    let name = catData[0];
    let age = catData[1];
    cats.push(new Cat(name, age));
  }

  for (const cat of cats) {
    cat.meow();
  }
}