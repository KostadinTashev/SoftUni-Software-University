function solve (people, groupType, day){
    let totalPrice = 0;
    switch (day) {
        case 'Friday':
            if (groupType === 'Students'){
                if (people >= 30){
                    totalPrice = people * 8.45 * 0.85;
                }else{
                    totalPrice = people * 8.45;
                }
            } else if (groupType === 'Business'){
                if (people >= 100){
                    totalPrice = (people-10) * 10.90;
                }else{
                    totalPrice = people * 10.90;
                }
            } else if (groupType === 'Regular'){
                if (people >= 10 && people <= 20){
                    totalPrice = people * 15 * 0.95;
                }else{
                    totalPrice = people * 15;
                }
            } 
            break;
            case 'Saturday':
                if (groupType === 'Students'){
                    if (people >= 30){
                        totalPrice = people * 9.80 * 0.85;
                    }else{
                        totalPrice = people * 9.80;
                    }
                } else if (groupType === 'Business'){
                    if (people >= 100){
                        totalPrice = (people-10) * 15.60;
                    }else{
                        totalPrice = people * 15.60;
                    }
                } else if (groupType === 'Regular'){
                    if (people >= 10 && people <= 20){
                        totalPrice = people * 20 * 0.95;
                    }else{
                        totalPrice = people * 20;
                    }
                } 
                break;
            case 'Sunday':
                if (groupType === 'Students'){
                    if (people >= 30){
                        totalPrice = people * 10.46 * 0.85;
                    }else{
                        totalPrice = people * 10.46;
                    }
                } else if (groupType === 'Business'){
                    if (people >= 100){
                        totalPrice = (people-10) * 16;
                    }else{
                        totalPrice = people * 16;
                    }
                } else if (groupType === 'Regular'){
                    if (people >= 10 && people <= 20){
                        totalPrice = people * 22.50 * 0.95;
                    }else{
                        totalPrice = people * 22.50;
                    }
                } 
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}