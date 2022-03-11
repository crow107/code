#include <stdio.h>
int sum(int*,int*);
int subtract(int*,int*);
int divide(int*,int*);
int multiply(int*,int*);
int sum(int *a,int *b){
    int Tsum;
    Tsum = *a+*b;
    printf("THe result is %d",Tsum);}
int subtract(int *a,int *b){
    int Tsum;
    Tsum = *a-*b;
    printf("THe result is %d",Tsum);}
int divide(int *a,int *b){
    int Tsum;
    Tsum = (*a )/ (*b);
    printf("THe result is %d",Tsum);}
int multiply(int *a,int *b){
    int Tsum;
    Tsum = (*a )* (*b);
    printf("THe result is %d",Tsum);}
int main(){
    int num1,num2,oppration;
    printf("Enter First Number :-");
    scanf("%d",&num1);
    printf("Enter Second Number :-");
    scanf("%d",&num2);
    printf("Enter \n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n:-");
    scanf("%d",&oppration);
    if(oppration == 1){
        sum(&num1,&num2);}
    else if(oppration == 2){
        subtract(&num1,&num2);}
    else if(oppration == 3){
        multiply(&num1,&num2);}
    else if(oppration == 4){
        divide(&num1,&num2);}}