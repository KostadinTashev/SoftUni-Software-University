function sameNumbers(number) {
   numberAsString = number.toString();
   let flag = false;
   let sum = 0;
//    for (let i = 0; i < numberAsString.length; i++) {
//     if(Number(numberAsString[i]) === Number(numberAsString[i+1])){
//         flag = true;
//     }else {
//         flag = false;
//     }
//     sum += Number(numberAsString[i]);
//    }
    for (const num of numberAsString) {
        step = 1;
        if(Number(numberAsString[step]) === Number(numberAsString[step+1])){
            flag = true;
        }else {
            flag = false;
        }
         
        sum += Number(numberAsString[step]);
        step +=1;    
    }
    
   console.log(flag);
   console.log(sum);
}

sameNumbers(1234);