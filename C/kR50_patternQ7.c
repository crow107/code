#include<stdio.h>
void main (){
    printf("kanishk rawat (BCA EA) \n");
    int n ;
    printf("Enter the value of n here:");
    scanf("%d",&n);
    for(int i =1;i<=n;i++){
        for (int k=1; k<=i ;k++){
            printf(" ");
        }
        for (int j=2*n-1;j>=(2*i)-1;j--){
            printf("*");

        }
        printf("\n");
    }
}