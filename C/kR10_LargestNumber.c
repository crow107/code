#include <stdio.h>
void main(){
    int a , b , c ,largest;
    printf("Enter 3 number");
    printf("\nfirst number:-");
    scanf("%d",&a);
    printf("\nSecond number:-");
    scanf("%d",&b);
    printf("\nThird number:-");
    scanf("%d",&c);
    largest = a>b? a>c?a:c : b>c? b:c;
    printf("The largest number is %d", largest); 

}