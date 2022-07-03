#include <stdio.h>

void main(){
    printf("Kanishk Rawat (BCA EA) \n");
    int even,sum=0, a=1;
    while (a<=50){
        even = 2*a;
        sum += even;
        a+=1;
    }
    printf("The sum of 50 even Numbers is %d ",sum);
}