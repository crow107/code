// Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered. 


import java.util.Scanner;


public class Questions07 {

    public static void main(String[] args) {
        int a =1;
        int positiveNum = 0;
        int negativeNum = 0;
        int zero = 0;
        while (a==1){
                Scanner sc = new Scanner(System.in);
                System.out.print("Enter Numbers:-");
                int num = sc.nextInt();
                if (num>0){
                    positiveNum = positiveNum +1;
                }
                else if(num<0){
                    negativeNum = negativeNum +1;
                }
                else{
                    zero = zero + 1;
                }
                System.out.println("what to add more Numbers (1-Yes/2-No)");
                int yes_no= sc.nextInt();
                if (yes_no==2){
                    a =2;
                    System.out.println("The number of zeros is "+zero);
                    System.out.println("The number of Negative Number is "+ negativeNum);
                    System.out.println("The number of Positive Numbers is "+positiveNum);
                }
                else{
                    a =1;
                }
            
            
        }
    }
}
