# include <stdio.h>

void main(){
    char Char_1;
    printf("Kanishk Rawat (BCA EA) \n");
    printf("Enter Anything:-");
    scanf("%c",&Char_1);
    if (Char_1>='a' && Char_1<='z'){
        printf("%c  is a LowerCase Alphabet .",Char_1);
    }
    else if(Char_1>='A' && Char_1<='Z'){
        printf("%c is a UpperCase Alphabet .", Char_1);

    }
    else{
        printf("Enter Alphabet Only");
    }
}