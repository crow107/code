#include <stdio.h>

void main(){
    printf("Kanishk Rawat (BCA EA) \n");
    int n, odd,sum=0, a=1;
    printf("Enter the value of N here :");
    scanf("%d",&n);
    while (a<=n){
        sum += a;
        a+=1;
    }
    printf("The sum of %d  Numbers is %d ",n,sum);
}