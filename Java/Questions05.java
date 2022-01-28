// Write a function that takes in age as input and returns if that person is eligible to vote or not. A person of age > 18 is eligible to vote.
import java.util.Scanner;


public class Questions05 {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter Your age :-");
            int age = sc.nextInt();

            if (age>=18){
                System.out.println("You are eligible for vote");

            }
            else{
                System.out.println("You are not eligible for vote");
            }
        }

    }
}
