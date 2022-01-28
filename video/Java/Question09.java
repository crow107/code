import java.util.Scanner;

//Write a function that calculates the Greatest Common Divisor of 2 numbers.


public class Question09 {
    
    public static void greatestCommonDivisor(int a , int b){
        int num= 0;
        if (a>b){
            for (int k = 1; k<=b;k++){
                if(a%k==0 || b%k==0){
                    num = k;
                    
                }
                
            }

        }
        else if(a<b){
            for (int k = 1; k<=a;k++){
                if(a%k==0 || b%k==0){
                    num = k;
                }
            }
            
        }
        else {
            for (int k = 1; k<=b;k++){
                if(a%k==0 || b%k==0){
                    num = k;
                }
            }
        }
        System.out.println(num);
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the first Number :-");
            int a = sc.nextInt();
            System.out.print("Enter the second Number:-");
            int b = sc.nextInt();
            greatestCommonDivisor(a, b);
        }
    }
    
}
