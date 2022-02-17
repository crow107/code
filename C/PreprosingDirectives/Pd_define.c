#include <stdio.h>

#define KA 10

void main(){
    #if KA 
    printf("ka is defined ");
    #else 
    printf("ka is not defined");
    #endif
}