#include <stdio.h>

void main(){
    int a ;
    printf("Enter your age :-");
    scanf("%d" , &a);

    if (a >= 18){
        printf("You are elegible to vote ");

    }
    else {
        printf("You are not elegible to vote " );

    }
}
