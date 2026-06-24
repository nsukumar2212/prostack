//print no of prices divisible by 3

let prices=[23,678,1055,34,544,554,43,786,]
let count=0;
for(const price of prices){
    if(price%3 ===0)
        console.log(price)
        count++

}
console.log("No of elements Divisible by3 is:",count)