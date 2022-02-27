#include <stdio.h>

int main(){
    int a = 4;
    int count=1;
    for(int i=0;i<a;i++){
        for(int j=0;j<i+1;j++){
            printf("%d ",count);
            count +=1;
        }
        printf("\n");
    }
}