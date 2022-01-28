// Write a function which takes in 2 numbers and returns the greater of those two.

import java.util.Scanner;

public class Questions03 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter Number_1 :-");
            int num_1 = sc.nextInt();
            System.out.print("Enter Number_2 :-");
            int num_2 = sc.nextInt();
            if (num_1>num_2){
                System.out.println(num_1 +" is greater than "+ num_2);
            
            }
            else if (num_2>num_1){
                System.out.println(num_2 +" is greater than "+ num_1);
            }
        }
        
    }
    
}
