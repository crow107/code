#include<stdio.h>

void main(){
    int i,n,count=0;
    printf("Kanishk Rawat (BCA EA)\n" );
    printf("Enter the value of N here: ");
    scanf("%d",&n);
    for (i=1;i<=n;i++){
        count +=i;
    }
    printf("The Sum Of N Number is : %d",count);

}
