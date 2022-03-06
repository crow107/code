#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    char strings[20] ;
    int flag = 0;
    printf("Enter the String greater than 2 character:-");
    fgets(strings,20,stdin);
    int length = strlen(strings)-1;
    if(length<3){
        printf("Enter the String greater than 2 character:-");
        fgets(strings,20,stdin);
    }
    else{
        for(int i =0;i<ceil(length/2);i++){
            if(strings[i]==strings[(length-i-1)]){
                flag= 1;
            }

        }
        if(flag==0){
            printf("No, It is not Palindrome");
        }
        else{
            printf("Yes, It is a Palindrome");
        }
    }

}