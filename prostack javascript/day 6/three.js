let employees =[
    {eid:101, ename:"RG", gender:'male'},
    {eid:102, ename:"RS", gender:'female'},
    {eid:103, ename:"RP", gender:'male'},
    {eid:104, ename:"SG", gender:'female'}

]

for(emp of employees){
    console.log(emp.ename)
}


let i=0;
while(i<employees.length){
    console.log(employees[i].ename);
    i++;
}
