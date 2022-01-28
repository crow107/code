// Enter 3 numbers from the user & make a function to print their average.

import java.util.Scanner;
public class Questions01{
    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the first Number:-");
            float num_1 = sc.nextFloat();
            System.out.print("Enter the Second Number:-");
            float num_2 = sc.nextFloat();
            System.out.print("Enter the Third Number:-");
            float num_3 = sc.nextFloat();
            float average = (num_1 + num_2 + num_3 )/3;
            System.out.printf("The average of three numbers is %f ", average);
        }
    }
}