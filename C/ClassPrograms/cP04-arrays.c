#include <stdio.h>

void main(){
    int marks[10];
    for (int i = 0;i<50;i++){
        scanf("%d",&marks[i]);
    }
    for (int i = 0; i<50;i++){
        printf("%d",marks[i]);
    }
}