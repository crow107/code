#include <stdio.h>

#define join(x,y) x##y

int main(){
    int a ;

    a = join(10,5);
    printf("%d " , a);

}