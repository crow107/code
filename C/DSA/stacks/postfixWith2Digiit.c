#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
    char name[50];
    int i;
    int stack[50];
    int top= -1;
    int ref= 48;
    int ex=0;
    
    printf("Format : Ex - a,b,c,+,- here a, b , c can be two digit no 3 digit no or can be any digit number");
    printf("Enter the Expression : ");
    fgets(name,50,stdin);

    for(i = 0;i<strlen(name)-1;){
        int Fnum; 
        if(ex==1){
            break;
        }
        else{
            Fnum = name[i]-ref;  // -2
            for(int j =1;j<strlen(name)-i-1;j++){ //25,
                
                if(name[i+j]==',' || name[i+j] ==')'){
                    if(j==1){
                        // printf("%d",Fnum);
                    }
                    if(name[i+j] ==')'){
                        int ex = 1;
                    }
                    // printf("\n");
                    i = i+j+1;
                    break;
                }
                else{
                    int num = name[i+j] -ref;
                    Fnum = Fnum*10 + num;
                    // printf("%d",Fnum);
                }
            }
            // -4 = , ,* = -6, - = -3 ,+ = -5,/ = -1 ,^ = 46,-7=),-8 =(
            // printf("%d",Fnum);
            if(Fnum==-1){// printf("/");
                int num1 = stack[top--];
                int num2 = stack[top];
                stack[top] = num2 / num1;
            }
            else if(Fnum == -3){// printf("-");
                int num1 = stack[top--];
                int num2 = stack[top];
                stack[top] = num2 - num1;
            }
            else if(Fnum== -5 ){// printf("+");
                int num1 = stack[top--];
                int num2 = stack[top];
                stack[top] = num2 + num1;
            }
            else if(Fnum== -6){// printf("*");
                int num1 = stack[top--];
                int num2 = stack[top];
                stack[top] = num2 * num1;
            }
            else if (Fnum == 46){// printf("^");
                int num1 = stack[top--];
                int num2 = stack[top];
                stack[top] = pow(num2,num1);
                
            }
            else{
                stack[++top] = Fnum;
            }
            
        }
        
        }
        printf("Ans = %d",stack[0]);
        
        
            
    }

