function printAndSum(startNum, endNum){
    let sum = 0;
    let output = '';
    for (let index = startNum; index <= endNum; index++) {
        output += String(index) + ' ';
        sum += index;
    }
    console.log(output);
    console.log(`Sum: ${sum}`);
}