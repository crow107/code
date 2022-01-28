//fibonachi series 1 1 2 3 5 8 13 21 ..

public class Question10 {
    public static void main(String[] args) {
        int n = 20;
        int x = 0;
        int y = 1;
        int z = 1;

        System.out.print( " 1 ");
        while(z<=n){
            System.out.print(" " +z+" ");
            x = y;
            y = z;
            z = x+y;


        }




        }
    }

