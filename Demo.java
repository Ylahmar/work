import java.util.Scanner;

public class Demo {

        public static void main(String[] args) {

                Scanner sc=new Scanner(System.in);

                int score=0;
                System.out.println("WELCOME TO ///LEVEL 1/// ANSWER THE PROBLEM CORRECTLY TO MOVE ON ");
                System.out.println("============================================================================");

                
         
                while(score<5)
                {
                        boolean pass=Level1Stage.askQuestion();
                        if(pass)
                                score++;
                }

                System.out.println("LEVEL 1 PASSED, YOU DID IT!!!!!!! NOW GET READY FOR LEVEL 2");
                System.out.println("///////// LEVEL 2 ///////////");
                System.out.println("============================================================================");
                score=0;
                
                while(score<5)
                {
                        boolean pass=Level2Stage.askQuestion();
                        if(pass)
                                score++;

                }

                System.out.println("LEVEL 2 PASSED, YOU DID IT!!!!!!! NOW GET READY FOR LEVEL 3");
                System.out.println("////////// LEVEL 3 ///////////");
                System.out.println("============================================================================");
                score=0;
                
                while( score<5)
                {
                        boolean pass=Level3Stage.askQuestion();
                        if(pass)
                                score++;
                }

                System.out.println("LEVEL 3 PASSED, CONGRATS YOU FINISHED!!!!!!!!!!");

        }

}
