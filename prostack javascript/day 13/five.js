class Account{
    min_bal=1000;

    deposit(){
        console.log("Deposit Sucessfully")
    }

    withdraw(){
        console.log("Withdraw Sucessfully")
    }

}

let a1=new Account()
a1.deposit()
a1.withdraw

let a2=new Account()
a2.deposit()
a2.withdraw()

console.log(a1)
console.log(a2)