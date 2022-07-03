#include <stdio.h>

void main(){
    char char1;
    printf("Kanishk rawat(BCA EA) \n");
    printf("Enter the Character:-");
    scanf("%c",&char1);
    if(char1>='a'&& char1<='z' || char1>='A'&& char1<='Z'){
        printf("%c Is a alphabet",char1);

    }
    else{
        printf("%c Is not a alphabet",char1);
    }
}