#include <stdio.h>

int main(){
    int numofStudent = 40;
    int totalSub = 5;
    int marks[40][5];
    for(int i =0;i<numofStudent;i++){
        for(int j=0;j<totalSub;j++){
            scanf("%d",&marks[i][j]);
        }
    }
    for(int i = 0;i<numofStudent;i++){
        for(int j =0; j<totalSub;j++){
            printf("%d",marks[i][j]);
        }
    }

}