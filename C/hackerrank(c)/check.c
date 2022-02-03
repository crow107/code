# include <stdio.h>
int inc(int *c);
void main (){
    int a = 27;
    inc(&a);
    printf("a = %d ",a);
}
int inc(int *c){
    (*c)++;
    printf("c = %d \n",*c);
}