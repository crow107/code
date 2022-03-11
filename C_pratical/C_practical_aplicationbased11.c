#include <stdio.h>
int main(){
    int a = 1;
    while(a==1){
    int num1,num2,oppration;
    float fnum1,fnum2;
    printf("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Average\n6.Percentage\n7.Exit\n:-");
    scanf("%d",&oppration);
    if(oppration == 1){
        printf("Enter First Number :-");
        scanf("%d",&num1);
        printf("Enter Second Number :-");
        scanf("%d",&num2);
        printf("The result is :- %d\n",num1+num2);
        
    }
    else if(oppration == 2){
        printf("Enter First Number :-");
        scanf("%d",&num1);
        printf("Enter Second Number :-");
        scanf("%d",&num2);
        printf("The result is :- %d\n",num1-num2);
    }
    else if(oppration == 3){
        printf("Enter First Number :-");
        scanf("%d",&num1);
        printf("Enter Second Number :-");
        scanf("%d",&num2);
        printf("The result is :- %d\n",num1*num2);
    }
    else if(oppration == 4){
        printf("Enter First Number :-");
        scanf("%f",&fnum1);
        printf("Enter Second Number :-");
        scanf("%f",&fnum2);
        printf("The result is :- %f\n",fnum1/fnum2);
    }
    else if(oppration == 5){
        printf("Enter First Number :-");
        scanf("%f",&fnum1);
        printf("Enter Second Number :-");
        scanf("%f",&fnum2);
        printf("The result is :- %f\n",(fnum1+fnum2)/2);
    }
    else if (oppration ==6){
        printf("Enter First Number :-");
        scanf("%f",&fnum1);
        printf("Enter Second Number :-");
        scanf("%f",&fnum2);
        printf("The result is :- %f %%\n",(fnum1+fnum2)/2);
    }
    else if (oppration ==7)
    {
        a=0;
    }
    else{
        printf("Enter the valid Number!!");
        a=0;
    }
    }
}