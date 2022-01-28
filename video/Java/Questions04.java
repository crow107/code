// Write a function that takes in the radius as input and returns the circumference of a circle.

import java.util.Scanner;


public class Questions04 {
    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the Radius :-");
            float radius = sc.nextFloat();
            float circumference = 2*3.14f*radius;
            System.out.println("The circumfrence of the circle is "+circumference);
        }
    
    }
    
}
