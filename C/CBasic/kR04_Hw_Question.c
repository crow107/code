#include <stdio.h>
// total average percentag
void main(){
    int a, b, c,d ,e ;
    float  Average, Percentage ,Total;
    printf("Enter the marks of \n Subject1- ");
    scanf("%d" , &a );
    printf("Subject2- ");
    scanf("\n%d" , &b );
    printf("Subject3- ");
    scanf("\n%d" , &c );
    printf("Subject4- ");
    scanf("\n%d" , &d );
    printf("Subject5- ");
    scanf("\n%d" , &e );
    Total = a + b + c + d + e;
    Average = Total /5;
    Percentage = Average;
    printf("Total mask obtained by the student is :- %0.f , Average marks is :- %0.f , and percentage is :- %0.2f ", Total ,Average , Percentage);
}