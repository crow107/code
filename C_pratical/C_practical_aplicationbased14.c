#include<stdio.h>
#include<conio.h>
int fact(int n);
int fibo();
int main(){
    int num;
    printf("Enter the Number Here:-");
    scanf("%d",&num);
    printf("The factorial of %d = %d\n",num,fact(num));
    printf("The fibonacci series upto %d =",num);
    fibo(num);}
int fact(int n){
    int b;
    if(n==1)
    return 1;
    b = n*fact(n-1);
    return b;}
int fibo(int n){
   int num1=0,num2=1;
   int sum;
   printf(" %d %d ",num1,num2);
   sum = num1+num2;
   while(sum<n){
       printf("%d ",sum);
       num1= num2;
       num2 = sum;
       sum = num1+num2;}
}