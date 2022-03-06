#include <stdio.h>

int main(){
    int Arr[]={1,2,3,4,5,6,7,8,9,0};
    int NumToSearch;
    int flag=0;
    printf("Enter the Number To Search = ");
    scanf("%d",&NumToSearch);

    for(int i=0;i<10;i++){
        if(NumToSearch ==Arr[i]){
            printf("Yes, The Number is in The Arr \n");
            flag = 1;
            break;
            
        }
    }
    if(flag==0){
        printf("No,The Nuber is Not in the Arr \n");

    }

    printf("The Arr in Descending order is = \n");
    for (int i=0;i<10;i++){
        for(int j = i+1;j<10;j++){
            if (Arr[i]>Arr[j]){
                int temp;
                temp = Arr[i];
                Arr[i]=Arr[j];
                Arr[j]= temp;
            }
        }
    }
    for (int i = 0;i<10;i++){
        printf("%d ",Arr[i]);
    }

}