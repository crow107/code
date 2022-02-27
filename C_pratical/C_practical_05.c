#include <stdio.h>

int main(){
    int Marks[50];
    int total=0;
    for(int i=0;i<50;i++){
        printf("Enter The Marks of Student %d =",i+1);
        scanf("%d",&Marks[i]);
    }
    for(int i=0;i<50;i++){
        total += Marks[i];
    }
    printf("The average Marks of The class is %d",total/50);
}