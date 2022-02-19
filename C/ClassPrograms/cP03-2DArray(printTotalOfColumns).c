#include <stdio.h>

void main(){
    int totalNumofStudent = 50;
    int totalSub = 4;
    int marks[50][4];
    for (int i = 0;i<totalNumofStudent;i++){
        for(int j =0; i<totalSub ;j++){
            scanf("%d",&marks[i][j])
        }
    }
    int sum = 0;
    for(int j = 0; j<totalNumofStudent;j++){
        int sum = 0;
        for(int j = 0;j<totalSub;j++){
            sum = sum+ marks[i][j];
        }
        printf("The sum of the marks is %d ",sum);
    }
}