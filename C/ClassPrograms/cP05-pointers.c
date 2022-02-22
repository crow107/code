# include <stdio.h>
void main(){
    int * p;
    int a = 10;
    p = &a;

    *p =20;


    printf("%d",*p);

    
}