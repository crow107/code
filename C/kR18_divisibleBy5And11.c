#include <stdio.h>

void main(){
    int Num;
    printf("Kanishk Rawat (BCA EA) \n");
    printf("Enter the Number to find it is divisible by 5 and 11 both or not:-");
    scanf("%d",&Num);

    if (Num%5==0 && Num%11==0){
        printf("%d Is divisible 5 and 11  ",Num);
    }
    else{
        printf("%d Is not divisible by 5 and 11 ",Num);
    }

}