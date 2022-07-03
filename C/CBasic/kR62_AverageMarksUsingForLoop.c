#include<stdio.h>

void main(){
    int i,n,marks ,count=0;
    printf("Kanishk Rawat (BCA EA)\n" );
    printf("Enter the Number of Student here:");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        printf("Enter the Marks Here: ");
        scanf("%d",&marks);
        count += marks;
    }
    printf("The average marks is : %d",count/n);
    
}