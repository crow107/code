
#include<stdio.h>
void main(){
    int num_1, num_2 , num_3;
    printf("Enter 3 numbers to find the greatest among them \n");
    printf("Enter number 1:-");
    scanf("%d",&num_1);
    printf("Enter number 2:-");
    scanf("\n%d",&num_2);
    printf("Enter number 3:-");
    scanf("\n%d",&num_3);
    if (num_1>num_2){
        if (num_1>num_3){
            printf("%d is the Greatest number", num_1);

        }
        if (num_1<num_3){
            printf("%d is the Greatest number", num_3);
        }
    
    }
    if (num_1<num_2){
        if (num_2>num_3){
            printf("%d is the Greatest number", num_2);

        }
        if (num_2<num_3){
            printf("%d is the Greatest number", num_3);
        }
    }


}