# include <stdio.h>

void main (){
    int count , n ,i =1;
    printf("Enter the Value of N:-");
    scanf("%d",&n);
    while (i<=n){
        count += 1;
        i++;
    }
    printf("Count = %d",count);
}