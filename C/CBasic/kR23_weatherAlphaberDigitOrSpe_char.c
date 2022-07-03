# include <stdio.h>

void main(){
    char Char_1;
    printf("Kanishk Rawat (BCA EA) \n");
    printf("Enter Anything:-");
    scanf("%c",&Char_1);
    if (Char_1>='a' && Char_1<='z' || Char_1>='A' && Char_1<='Z'){
        printf("%c  is a Alphabet .",Char_1);

    }
    else if (Char_1>='1' && Char_1<='9'){
        printf("%c is a Digit" , Char_1);
    }
    else{
        printf("%c is a special Character.",Char_1);
    }

}