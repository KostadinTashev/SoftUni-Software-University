function cookingByNumbers(numberAsString, ...array){
    operations = array;
    number = Number(numberAsString);
    for (const operation of operations) {
        if (operation === 'chop'){
            number = number / 2;
        }else if (operation === 'dice'){
            number = Math.sqrt(number);
        }else if (operation === 'spice'){
            number += 1
        }else if (operation === 'bake'){
            number *= 3
        }else {
            number -= number *  0.2;
        }
        console.log(number);
    }
}

// cookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop');
cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet');