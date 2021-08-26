import java.util.Random;

public class Data {
        public static int getRandomNumber(int low,int high)
        {
                Random rand=new Random();
                return rand.nextInt(high - low) + low;
        }
}
