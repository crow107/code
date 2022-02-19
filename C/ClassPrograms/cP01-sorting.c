#include <stdio.h>

int main(){
    int totalNumberofStudent = 40;
    int marks[40];
    int a;
    for(int i=0;i<totalNumberofStudent;i++){
            scanf("%d",&marks[i]);
    }
    for(int i=0; i<totalNumberofStudent; i++)
    {
        for (int j =i+1;j<totalNumberofStudent;j++){
            if(marks[i]<marks[j]){
                a = marks[i];
                marks[i]= marks[j];
                marks[j] = a ;
            }
        }
    }

