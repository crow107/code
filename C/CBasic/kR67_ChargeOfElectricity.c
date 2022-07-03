#include<stdio.h>

void main(){
    int n,price=0;
    printf("Kanishk Rawat (BCA EA)\n" );
    printf("Enter the Electricity Unit here:");
    scanf("%d",&n);
    if (n<=50 && n>0){
        price = price +(0.5*n);

    }
    else if(n<=150 && n>50){
        price = price +(0.5*50);
        n = n-50;
        price = price +(0.75*n);
    }
    else if(n<=250 && n>150){
        price = price +(0.5*50);
        price = price +(0.75*100);
        n =  n - 150;
        price = price + (1.2*n);

    }
    else if(n>250){
        price = price +(0.5*50);
        price = price +(0.75*100);
        price = price + (1.2*n);
        n = n -250;
        price = price + (1.5*n);

        
    }
    printf("The Price of The Electricity Unit is %d",price);
}