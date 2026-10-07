class Account {
    min_Bal = 500;
    constructor(id, name, amount) {
        this.acc_Id = id;
        this.acc_Name = name;
        this.acc_Bal = amount;
    }

    openAccount() {
        console.log("Account opened");
    }

    deposit(amount) {
        this.acc_Bal = this.acc_Bal + amount;
    }

    withdraw(amount) {
        this.acc_Bal = this.acc_Bal - amount;
    }

    get_bal() {
        return this.acc_Bal-this.min_Bal;
    }
}

let a1 = new Account(101, "Rahul", 6000);
a1.deposit(4000);

let a2 = new Account(102, "Sonia", 7000);
a2.deposit(5000);

let a3 = new Account(103, "Priya", 8000);
a3.deposit(6000);

console.log(a1);
console.log(a2);
console.log(a3);