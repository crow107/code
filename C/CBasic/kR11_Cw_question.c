# include <stdio.h>
void main(){
    int Marks ;
    printf("Enter your marks");
    scanf("%d",&Marks);
    if (Marks>=90){
        printf("Grade = A");
    }
    if ((Marks>=80)&& (Marks<=89)){
        printf("Grade = B");
    }
    if ((Marks>=70)&&(Marks<=79)){
        printf("Grade = C");
    }
    if (Marks<=70){
        printf("Grade = D");
    }

}
