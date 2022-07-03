#include <stdio.h>

void main(){
    int Salary  ,tax ;
    printf("Enter your salary :- ");
    scanf("%ld" , &Salary);
    if (Salary < 500000 && Salary > 250000){
        tax = (Salary *5 )/100;
        printf("Your tax is %ld " , tax);
    }
    else if (500000 < Salary && Salary < 1000000){
        tax = (Salary * 20)/100;
        printf("Your tax is %ld " , tax);
    }
    else if (Salary > 1000000){
        tax = (Salary * 30)/100;
        printf("Your tax is %ld " , tax);
    }
    else{
        printf("Your tax is 0");
    }
}
