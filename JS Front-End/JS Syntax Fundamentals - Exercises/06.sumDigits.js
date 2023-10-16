function sumDigits(number){
    let sum = 0;
    stringNumber = String(number);
    for (const el of stringNumber) {
        sum += Number(el);
    }
    console.log(sum)
}