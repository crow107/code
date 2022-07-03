#include <stdio.h>

int main(){
    char char1;
    printf("kanishk Rawat (BCA EA) \n");
    printf("Enter an Alphabet:-");
    scanf("%c",&char1);
    if (char1 =='a'||char1 =='e'||char1 =='i'||char1=='o'||char1=='u'||char1=='A'||char1 =='E'||char1 =='I'||char1=='O'||char1=='U'){
        printf("%c Is a vowel ",char1);
    }
    else{
        printf("%c Is a constant ",char1);
    }

}