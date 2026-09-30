/*  let a=[10,20,30,40]
let b=[30,40,50,60]
let c=[...a,...b]
console.log(c)
 


let emp={
    eid:101,
    ename:"RG",
    email:"rg@gmail.com"
}

let details={
    esal:45000, 
    email:"rg@gmail.com"
}

let emp_details={...emp, ...details}
console.log(emp_details) */

function add(a,...b){
    console.log("a-:",a,"****","b:",b)

}

add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)