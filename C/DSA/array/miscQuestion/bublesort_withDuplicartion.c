# include <stdio.h>



int main(){
    int arr[50],i,j,temp,n,newarr[10];          // taking array
    printf("How many element you want");
    scanf("%d",&n);
    for(i=0;i<n;i++){                   // with for loop
        printf("Enter the value at %d index :-  ",i); // insert the values into the array
        scanf("%d",&arr[i]);                
    }
    printf("Unsorted array \n");
    for(i=0;i<n;i++){                   // printing unsorted array
        printf("%d ",arr[i]);
    }
    printf("\n");

    for(i=0;i<n-1;i++){
        for(j=0;j<(n-i-1);j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j]=arr[j+1];
                arr[j+1] =temp;
            }
        }
    }
    
    printf("sorted array \n");
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");

    int q =0;
    printf("repeted elements");
    for(i=0;i<n;i++){
        int count=0;
        for(j=0;j<n;j++){
            if(arr[i]!=newarr[j] && i!=j){
                count++;
            }
        }
        if(count==n-1){
            newarr[q]= arr[i];
            q++;
        }        
    }


    for(i=0;i<q;i++){
        int count = 0;
        for(j=0;j<n;j++){
            if(newarr[i]==arr[j]){
                count++;
            }
        }
        if(count>1){
        printf("%d occurs %d time \n",newarr[i],count);}
    }
}