# include <stdio.h>

void main (){
    int t1 = 0;
    int t2 = 1,sum =0 ;
    printf("Enter the value of N :");
    scanf("%d",&n);
    for (int i=1; i<=n;i++){
        sum = t1 +t2;
        t1,t2 = t2,sum;
        

    }
}