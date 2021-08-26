class Cargo extends Ship
{

   int capacity;
   public Cargo(String name, String year,int capacity) {
       super(name, year);
       this.capacity=capacity;
   }
   @Override
   public String toString() {
       return "Cargo [ name=" + name + ", capacity=" + capacity + "]";
   }
   public int getCapacity() {
       return capacity;
   }
   public void setCapacity(int capacity) {
       this.capacity = capacity;
   }
  
}