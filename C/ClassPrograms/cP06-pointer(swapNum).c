#include <stdio.h>
int pointer(Num1,Num2);
void main(){
    int Num1,Num2;
    Num1 = 100;
    Num2 = 20;

    pointer(Num1,Num2);
}

int pointer(&x,&y){
    int * Num1;
    int * Num2;
    Num1 = x;
    Num2 = y;
}