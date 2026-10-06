class Account{
    min_Bal=500;
    open_Account(){
        console.log("Account Opened")
    }
    deposit(){
        console.log("Deposit Sucessfully")
    }
    withdrawl(){
        console.log("Withdrawl Sucessfully")
    }
    get_Bal(){
        console.log("Getting Balance")
    }
    close_Account(){
        console.log("Account Closed")
    }
}
let a1=new Account()
console.log(a1.min_Bal)
a1.open_Account()
a1.deposit()
a1.withdrawl()
a1.get_Bal()
a1.close_Account()