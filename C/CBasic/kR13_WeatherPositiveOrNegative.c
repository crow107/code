#include <stdio.h>

void main(){
    int Num;
    printf("kanishk Rawat (BCA EA) \n");
    printf("Enter The Number : ");
    scanf("%d" , &Num);

    if (Num > 0 ){
        printf("\" %d is Positive Number \"",Num);

    }
    else if(Num < 0 ){
        printf("\" %d is Negative Number\"",Num); 
    }
    else {
        printf("\"Ther Number is 0\"" );

    }
}