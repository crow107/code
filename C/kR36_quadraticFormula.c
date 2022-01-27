#include <stdio.h>
void main(){
    printf("Kanishk Rawat (BCA EA)\n");
    // d = b*b - 4*a*c
    int  d , b, a ,c;
    printf("Enter the Value of A:-");
    scanf("%d",&a);
    printf("Enter the Value of B:-");
    scanf("%d",&b);
    printf("Enter the Value of C:-");
    scanf("%d",&c);

    d = (b*b) - (4*a*c);
    if(d >0){
        printf("Two different Real roots");
    }
    else if (d<0){
        printf("No real Roots");
    
    }
    else if (d==0){
        printf("Two same Real roots");
    }


}