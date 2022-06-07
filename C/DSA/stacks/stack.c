#include <stdio.h>

int main(){
    int n,i,j;
    printf("Enter the Size of stack : ");
    scanf("%d",&n);
    int arr[n];
    int a = 1;
    int k;
    int item = -1;
    while (a==1)
    {  
        printf("STACK \n");
        for(i = n-1;i>=0;i--){
            printf("|\t%d\t|\n",arr[i]);

        }
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Exit\n");
        scanf("%d",&k);
        if(k==1){
            if(item >=n-1){
                printf("Stack overflow\n");
                break;
            }
            else{
                printf("Enter the value at %d index stack : ",item+1);
                scanf("%d",&arr[++item]);
            }
            
        }
        else if(k==2){
            if(item== -1){
                printf("Stack underflow\n");
                break;
            }
            else{
                
                printf("Poped Element is %d ",arr[item]);
                arr[item--] =0;

            }
        }
        else if(k==3){
            a=0;
        }
        else{
            a=0;
        }
    }
    
}

