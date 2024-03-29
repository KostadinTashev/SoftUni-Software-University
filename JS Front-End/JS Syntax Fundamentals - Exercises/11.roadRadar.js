function roadRadar(speed, area){
    let speedLimit;
    let status = '';
    let difference = 0;
    switch (area) {
        case 'motorway':
            speedLimit = 130;
            difference = speed - speedLimit;
            if (speed <= speedLimit){
                console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
                break;
            } else if (difference <= 20){
                status = 'speeding';
                difference = speed - speedLimit;
            } else if (difference <= 40){
                status = 'excessive speeding';
                difference = speed - speedLimit;
            }else {
                status = 'reckless driving';
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
            break;

        case 'interstate':
            speedLimit = 90;
            difference = speed - speedLimit;
            if (speed <= speedLimit){
                console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
                break;
            } else if (difference <= 20){
                status = 'speeding';
                difference = speed - speedLimit;
            } else if (difference <= 40){
                status = 'excessive speeding';
                difference = speed - speedLimit;
            }else {
                status = 'reckless driving';
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
            break;
        
        case 'city':
            speedLimit = 50;
            difference = speed - speedLimit;
            if (speed <= speedLimit){
                console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
                break;
            } else if (difference <= 20){
                status = 'speeding';
                difference = speed - speedLimit;
            } else if (difference <= 40){
                status = 'excessive speeding';
                difference = speed - speedLimit;
            }else {
                status = 'reckless driving';
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
            break;

        case 'residential':
            speedLimit = 20;
            difference = speed - speedLimit;
            if (speed <= speedLimit){
                console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
                break;
            } else if (difference <= 20){
                status = 'speeding';
                difference = speed - speedLimit;
            } else if (difference <= 40){
                status = 'excessive speeding';
                difference = speed - speedLimit;
            }else {
                status = 'reckless driving';
            }
            console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
            break;
        default:
            break;
    }
}