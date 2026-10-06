let goToBNK=(Sucess,Failure)=>{
    let acc_bal=80000
    if(acc_bal>70000){
        Sucess("Go&Enjoy")
    }
    else{
        Failure("Go to prostack")
    }
}

goToBNK((msg)=>{},()=>{})

goToBNK((msg)=>{console.log(msg)},(err)=>{console.log(err)})