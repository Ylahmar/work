import java.io.File;
import java.io.FileNotFoundException;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
class Ship implements Comparable<Ship>
{
   String name;
   String year;
   public String getName() {
       return name;
   }
   public void setName(String name) {
       this.name = name;
   }
   public String getYear() {
       return year;
   }
   public void setYear(String year) {
       this.year = year;
   }
   public Ship(String name, String year) {
      
       this.name = name;
       this.year = year;
   }
  
   public String toString() {
       return "Ship [name=" + name + ", year=" + year + "]";
   }
   @Override
   public int compareTo(Ship o) {
       return this.year.compareTo(o.year);
   }
  
}

