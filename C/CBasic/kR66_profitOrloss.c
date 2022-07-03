#include<stdio.h>

void main(){
    int i, num_1 ,num_2;
    printf("Kanishk Rawat (BCA EA)\n" );
    printf("Enter the buying price :");
    scanf("%d/n",&num_1);
    printf("Enter the Selling price :");
    scanf("%d/n",&num_2);
    if (num_1>num_2){
        printf("Loss of %d",num_1-num_2);
    }
    else if (num_2>num_1)
    {
        printf("Profit of %d",num_2-num_1);
    }
    

}