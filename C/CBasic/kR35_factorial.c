# include <stdio.h>
void main(){
    int n ;
    int fact = 1;
    printf("Enter the Number to get its factorial :");
    scanf("%d"&n);
    for (int i = 1 ; i<=n; ;i++){
        fact = fact * i;

    }
    printf("The factorial of %d is %d ",n,fact)
}

