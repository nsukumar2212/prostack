class Account{
    acc_bal=0
    deposit(amount){
        this.acc_bal=this.acc_bal+amount;
    }
    withdraw(amount){
        this.acc_bal=this.acc_bal-amount;
    }
}

let a1=new Account();
let a2=new Account();
console.log(a1)
console.log(a2)
a1.deposit(1000);
a1.deposit(500);
a2.deposit(500);
a2.deposit(1500);
a1.withdraw(200);
console.log(a1.acc_bal);
console.log(a2.acc_bal);