class CruiseShip extends Ship
{
   int numOfPassenger;
   public CruiseShip(String name, String year,int num) {
       super(name, year);
       numOfPassenger=num;
   }
   public int getNumOfPassenger() {
       return numOfPassenger;
   }
   public void setNumOfPassenger(int numOfPassenger) {
       this.numOfPassenger = numOfPassenger;
   }

   public String toString() {
       return "CruiseShip [name=" + name + ", year=" + year +", numOfPassenger=" + numOfPassenger/2 + "]";
   }  
  
}