import java.util.Scanner;

class kR01{
    public static void addTwoNumber(int Num_1 , int Num_2 ){
        int sum;
        sum = Num_1 + Num_2;
        System.out.printf("The sum of %d and %d is %d" ,Num_1,Num_2,sum);
        return ;
    }


    public static void main(String[] args){
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the First Number:- ");
            int Num_1 = sc.nextInt();
            System.out.print("Enter the Second Number: -");
            int Num_2 = sc.nextInt();
            addTwoNumber(Num_1, Num_2);
        }

    }
}