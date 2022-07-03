# include<stdio.h>
void prime (int);

void prime (int a)
{
    int m=a/2,check=0;
    for(int i=2;i<=m;i++)    
    {    
        if(a%i==0)    
        {    
        printf("%d is not prime Number",a);    
        check=1;    
        break;    
        }    
    }    
    if(check==0)    
    printf("%d is prime number",a);     
    }  

int main(){  
int n;      
printf("Enter the number to check prime:");    
scanf("%d",&n);

prime(n);


} 
    
