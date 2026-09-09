let employees =
[
    {
        "eid": 1,
        "ename": "Rahul",
        "gender": "Male"
    },
    {
        "eid": 2,
        "ename": "Sonia",
        "gender": "Female"
    },
    {
        "eid": 3,
        "ename": "Priyanka",
        "gender": "Female"
    },
    {
        "eid": 4,
        "ename": "Modi",
        "gender": "Male"
    },
    {
        "eid": 5,
        "ename": "Amith",
        "gender": "Male"
    },
    {
        "eid": 6,
        "ename": "Alia",
        "gender": "Female"
    },
    {
        "eid": 7,
        "ename": "Keerty Suresh",
        "gender": "Female"
    },
    {
        "eid": 8,
        "ename": "Rashmika Mandanna",
        "gender": "Female"
    },
    {
        "eid": 9,
        "ename": "Nayanatara",
        "gender": "Female"
    },
    {
        "eid": 10,
        "ename": "Vijay Setupathi",
        "gender": "Male"
    },
    {
        "eid": 11,
        "ename": "Vijay",
        "gender": "Male"
    },
    {
        "eid": 12,
        "ename": "Ajith",
        "gender": "Male"
    },
    {
        "eid": 13,
        "ename": "Pawan kalyan",
        "gender": "Male"
    },
    {
        "eid": 14,
        "ename": "Allu Arjun",
        "gender": "Male"
    },
    {
        "eid": 15,
        "ename": "Mr Revanth Reddy",
        "gender": "Male"
    },
    {
        "eid": 16,
        "ename": "Rukmini",
        "gender": "Female"
    },
    {
        "eid": 17,
        "ename": "KTR",
        "gender": "Male"
    },
    {
        "eid": 18,
        "ename": "Chandrababu",
        "gender": "Male"
    },
    {
        "eid": 19,
        "ename": "Jagan",
        "gender": "Male"
    },
    {
        "eid": 20,
        "ename": "DK Shiva",
        "gender": "Male"
    }
]

for (let emp of employees) {
    if (emp.gender == "Male") {
        console.log(emp.ename);
    }
}


let mcount = 0;
let fcount = 0;

let i=0;
while(i<=employees.length-1){
    if(employees[i].gender=="Male"){
        mcount++;
    }
    i++;

}
console.log(mcount);