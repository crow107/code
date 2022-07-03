# include <stdio.h>

void main (){
    int n;
    int t1 = 0;
    int t2 = 1,sum =0 ;
    printf("Enter the value of N :");
    scanf("%d",&n);
    printf("%d %d",t1,t2);
    for (int i=1; i<=n;i++){
        sum = t1 +t2;
        printf("%d ",sum);
        t1=t2;
        t2 =sum;

    }
}