import java.util.Scanner;
public class kR03 {
    public static void factorial(int a){
        int total =1;
        for(int p = 1; p<=a;p++){
            total = total * p;
        }
        System.out.println(total); 
        return;
        
    }
    public static void main (String[] args){
    try(Scanner sc = new Scanner(System.in)){
        System.out.print("Enter the Number to get it's factorial :- ");
        int a = sc.nextInt();
        factorial(a);
    }
    }
}
