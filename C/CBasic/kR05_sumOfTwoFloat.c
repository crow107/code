#include <stdio.h>

void main (){
    float A , B , C;
    char D;
    printf("Enter 2 float numbers to get the sum of the numbers:- \n V  V \n");
    scanf("%f %f", &A , &B);
    printf("Enter a Character :- ");
    scanf("\n%c" , &D);
    
    C = A + B ;
    printf("The sum of two float numbers %0.1f and %0.1f is %0.2f",A , B , C);
    printf("The  Character you entered is :- %c" ,D);

}