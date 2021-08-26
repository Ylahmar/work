import java.util.Random;
import java.util.Scanner;

public class Level2Stage {

        public static boolean askQuestion()
        {
                Scanner sc=new Scanner(System.in);
                Random rand=new Random();
                int num1=0;
                int num2=0;
                int triesCount=0;

                num1=Data.getRandomNumber(1, 10);
                num2=Data.getRandomNumber(1, 10);
                while(triesCount<2)
                {
                System.out.println("What is "+num1+" + "+num2+"?");
                int ans=sc.nextInt();
                if(ans==num1+num2)
                {
                        System.out.println("Right answer! GREAT JOB");
                        return true;
                }
                else
                {
                        System.out.println("Wrong answer! TRY AGAIN YOU GOT IT ");
                        triesCount++;
                }
                }

                return false;
        }
}