#include<stdio.h>
void main (){
    printf("kanishk rawat (BCA EA) \n");
    int n ;
    printf("Enter the value of n here:");
    scanf("%d",&n);
    for(int i =1;i<=n;i++){
        for (int j=1;j<=(n-i+1);j++){
            printf("%d",j);

        }
        printf("\n");
    }
}