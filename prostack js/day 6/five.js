let emp={
    eid:101,
    ename:"rg",
    email:'rg@example.com'
}
let details={
    email:'rg@example.com',
    esal:45000,
    loc:'blr'
}
let empdetails={...emp,...details}
console.log(empdetails)