#include <stdio.h>

void main(){
    printf("Kanishk Rawat (BCA EA) \n");
    int odd,sum=0, a=1;
    while (a<=50){
        odd = 2*a-1;
        sum += odd;
        a+=1;
    }
    printf("The sum of 50 even Numbers is %d ",sum);
}