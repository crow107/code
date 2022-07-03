#include<stdio.h>
void main (){
    printf("kanishk rawat (BCA EA) \n");
    int n ,count=1;
    printf("Enter the value of n here:");
    scanf("%d",&n);
    for(int i =1;i<=n;i++){
        for (int j=1;j<=i;j++){
            printf("%d",count);
            count += 1;

        }
        printf("\n");
    }
}