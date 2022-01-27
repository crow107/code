# include <stdio.h>
void main (){
    printf("kanishk rawat (BCA EA) \n");
    int side_1, side_2 , side_3;
    printf("Enter first side - ");
    scanf("\n%d",&side_1);
    printf("Enter Second side - ");
    scanf("\n%d",&side_2);
    printf("Enter Third side - ");
    scanf("\n%d",&side_3);
    if (side_1 + side_2 >side_3 && side_3+side_2 >side_1 &&side_2+side_1>side_3){ 
        printf("Yes, the triangle is Valid");

    }
    else{
        printf("No, the triangle is no Valid");
    }
}
