// Two numbers are entered by the user, x and n. Write a function to find the value of one number raised to the power of another i.e. xn
import java.util.Scanner;
public class Questions08 {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the first Number:-");
            double x = sc.nextInt();
            System.out.print("Enter the second Number:-");
            double n = sc.nextInt();
            System.out.println(Math.pow(x,n));
        }
    }
}
