import java.util.Scanner;

public class kR02 {
    public static void productOfTwoNumbers(int Num_1 ,int Num_2){
        int product = Num_1 * Num_2;
        System.out.println("The Product is " + product);
        return;
    }

    public static void main(String[] args){
        try(Scanner sc = new Scanner(System.in)){
        
            System.out.print("Enter the first Number here :=");
            int Num_1 = sc.nextInt();
            System.out.print("Enter the second Number here :=");
            int Num_2 = sc.nextInt();
            productOfTwoNumbers(Num_1, Num_2);
            
        }
    
    }
}