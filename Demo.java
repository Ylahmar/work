import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
public class Demo {
    
    public static void main(String[] args) {
        Ship[] list= new Ship[10];
        try {
            Scanner scanner=new Scanner(new File("Shipinfo.txt"));
            
            int i=0;
            while (scanner.hasNextLine()) {
                String data[] = scanner.nextLine().split(":");
                String temp=data[2].trim();
                if(temp.equals("Ship")){
                    list[i++]=new Ship(data[0].trim(),data[1].trim());
                }
                else if(temp.equals("CruiseShip")) {
                    list[i++]=new CruiseShip(data[0].trim(),data[1].trim(),Integer.parseInt(data[3].trim()));
                }
                else if(temp.equals("CargoShip"))
                {
                    list[i++]=new Cargo(data[0].trim(),data[1].trim(),Integer.parseInt(data[3].trim()));
                }
            }
            scanner.close();
            } catch (FileNotFoundException e) {
                System.out.println("An error, There isnt a file with that name.");
                e.printStackTrace();
            }
            for(int i=0;i<list.length;i++)
            {
                System.out.println(list[i].toString());
            }
            //System.out.println("---------------------------------------");
            Arrays.sort(list);
            System.out.println("----------------------------------------");
            System.out.println("\n\n--------After sorting According to the year :------ \n\n");
            System.out.println("-----------------------------------------");
            for(int i=0;i<list.length;i++)
            {
                System.out.println(list[i].toString());
            }
        }
    }
    
                
                    
                    
                
                    
                
                
                
            
            
            