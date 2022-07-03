# include <stdio.h>

void main(){
    printf("Kanishk rawat (BCA EA) \n");
    int a1,a2,a3;
    printf("Enter first angle - ");
    scanf("\n%d",&a1);
    printf("Enter Second angle - ");
    scanf("\n%d",&a2);
    printf("Enter Third angle - ");
    scanf("\n%d",&a3);
    if (a1 + a2 + a3 ==180){
        printf("Yes, the triangle is Valid");

    }
    else{
        printf("No, the triangle is no Valid");
    }
}