# include <stdio.h>
#include <string.h>

int main(){
    char name[20],i;
    printf("Enter your name-");
    gets(name);
    char uniquename[20];
    int j = 0;


    // to find the unique letter in the name
    for(i=0;i<strlen(name);i++){
        if(strchr(uniquename,name[i])==0){
            uniquename[j]=name[i];
            j++;
           
        }

    }

    // this is used to create the uniquename(character arr ) To sting
    uniquename[j]='\0';
    

    // sorting of the new array
    for(i=0;i<strlen(uniquename);i++){
         for(j=i+1;j<strlen(uniquename);j++){
            if(uniquename[i]>uniquename[j]){
                int temp = uniquename[i];
                uniquename[i] = uniquename[j];
                uniquename[j] = temp;
            }
        }
    }
    printf("%s",uniquename);
    

}