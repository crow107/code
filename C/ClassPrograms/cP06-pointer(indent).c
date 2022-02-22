#include <stdio.h>
int incriment(Num);
int main(){
    int Num = 1;
    incriment(Num);
    printf("%d",Num);
}

int incriment(Num){
    int * p;
    p = &Num;

    *p++;
}