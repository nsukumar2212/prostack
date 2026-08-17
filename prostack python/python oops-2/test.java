class Account{
    Account(){
        System.out.println("Test Class - constructor method - special jilebi");
    }
    public void deposit(){
        System.out.println("deposit - normal method");
    }
    public static void main(String[] args) {
      Account t1=new Account();
      Account t2=new Account();
      Account t3 =new Account();
    }
}