let gotoMovie=(sucess,failure)=>{
    let acc_bal=1100;
    if(acc_bal>500){
        sucess("Enjoy the movie");
    }
    else{
        failure("Go to pg");
    }
};

gotoMovie((msg)=>{console.log(msg)}, (err)=>{console.log(err)});