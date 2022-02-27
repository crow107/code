// WAP to check that the Number is prime or Not

# include <stdio.h>

int main(){
    int n,check;
    printf("Enter The Number here :=");
    scanf("%d",&n);
    for(int i=1;i<n/2;i++){
        if(n%i==0){
            printf("%d is Not a Prime Number");
            check += 1;
            break;
        }
    }
    if (check==0){
        printf("%d is a Prime Number.",n);
    
}
