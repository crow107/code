#include <stdio.h>

void main(){
    int Num;
    printf("Enter The Number : ");
    scanf("%d" , &Num);
    
    if (Num > 0 ){
        if (Num %2 == 0){
            printf("\" %d is Positive Even Number\"",Num);

        }
        else {
            printf("\" %d is Positive Odd Number\"",Num); 
        }
    }
    else {
        if (Num %2 == 0){
            printf("\" %d is Negative Even Number\"",Num); 
        }
        else{
            printf("\" %d is Negative Odd  Number\"",Num); 
        }
    
}
}