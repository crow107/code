#include <stdio.h>

int main(){
    int size,i;
    printf("Enter the size of queue");
    scanf("%d",&size);
    int queue[size];
    int rare=-1;
    int front=-1;
    int stop =0;
    while(stop==0){
        printf("1.Insertion in queue \n");
        printf("2.Deletion in queue \n");
        printf("3.Print the queue \n");
        printf("4.Exit \n");

        int ans;
        printf("Enter here :- \n");
        scanf("%d",&ans);
        int num;
        switch (ans)
        {
        case 1:
            
            
            if(rare >=size-1){
                printf("Queue overflow \n");

            }
            else{
                printf("Enter the Number To insert :- ");
                scanf("%d",&num);
                
                if(rare==-1 && front==-1){
                    front=0;
                    rare=0;
                    queue[rare] = num;
                    printf("Inserted at hi front = %d rare = %d \n",front,rare); 
                }
                else{
                    queue[++rare] = num;
                    printf("Inserted at front = %d rare = %d \n",front,rare); 

                }
            }
            printf("\n");
            break;
        case 2:
            if(rare==front==-1){
                printf("Queue Underflow \n");
            }
            else{
                printf("%d \n",queue[--front]);
            }
        
            break;
        case 3:
            for(i=front;i<=rare;i++){
                printf("%d \n ",queue[i]);
            }
        default:
            break;
        }

        
    }
}