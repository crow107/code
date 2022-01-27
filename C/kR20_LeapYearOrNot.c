#include <stdio.h>

void main(){
    int Year;
    printf("kanishk rawat (BCA EA) \n");
    printf("Enter the Year (ex- 2021):-");
    scanf("%d",&Year);
    if(Year%4==0 && Year%100!=0){
        printf("%d Is a leap year",Year);
    }
    else if(Year%400==0){
        printf("%d Is a leap year",Year);

    }
    else{
        printf("%d Is not a leap year",Year);
    }
}