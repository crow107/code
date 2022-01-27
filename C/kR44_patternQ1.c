#include<stdio.h>
void main (){
    printf("kanishk rawat (BCA EA) \n");
    int n ;
    printf("Enter the value of n here:");
    scanf("%d",&n);
    for(int i =0;i<=n;i++){
        for (int j=0;j<=i;j++){
            printf("*");

        }
        printf("\n");
    }
}