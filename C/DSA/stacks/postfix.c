#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
    char name[20],i;
    int stack[20];
    int top= -1;
    int ref= 48;
    printf("Enter The Expression : ");
    fgets(name,20,stdin);
    // * = -6, - = -3 ,+ = -5,/ = -1 ,^ = 46
    for(int i = 0 ; i <strlen(name)-1;i++){
        int otp = name[i] -ref;
        // printf("%d",otp);
        if(otp==-1){// printf("/");
            int num1 = stack[top--];
            int num2 = stack[top];
            stack[top] = num1 / num2;
        }
        else if(otp == -3){// printf("-");
            int num1 = stack[top--];
            int num2 = stack[top];
            stack[top] = num1 - num2;
        }
        else if(otp== -5 ){// printf("+");
            int num1 = stack[top--];
            int num2 = stack[top];
            stack[top] = num1 + num2;
        }
        else if(otp== -6){// printf("*");
            int num1 = stack[top--];
            int num2 = stack[top];
            stack[top] = num1 * num2;
        }
        else if (otp == 46){// printf("^");
            int num1 = stack[top--];
            int num2 = stack[top];
            stack[top] = pow(num1,num2);
             
        }
        else{
            stack[++top] = otp;
        }
        
    }
    printf("Ans = %d",stack[0]);


}