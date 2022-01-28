// Write a function to print the sum of all odd numbers from 1 to n.


public class Questions02 {
    public static void main(String[] args) {
        int n = 10 ;
        int sum_odd = 0;
        int sum_even = 0;
        for(int a = 1; a<=n;a++ ){
            if (a%2!=0){
                sum_odd = sum_odd +a;
            }
            else{
                sum_even = sum_even + a;
            }
            
        }
        System.out.println("The sum of odd numbers is -"+sum_odd);
        System.out.println("The sum of even numbers is -"+sum_even);
    }
    
}
