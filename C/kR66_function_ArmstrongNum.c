#include <stdio.h>
int digits(int);
int armstrongsum(int,int);
int main()
{
    printf("Enter the range ");
    scanf("%d",&max);

}
int digits(int max )
{
    int digits = 0;
    while (n1!=0)
    {
        n1= n1/10;
        digits++;
    }
    return digits;
        
}
int armstrongsum(int a ,int digits)
{
    int digit,n2=a, sum=0;
    while (n2!=0)
    {
        digit = n2%10;
        sum = sum + pow(digit,digits);
        n2=n2/10;

    }
    
}