#include <stdio.h>

void main(){
    printf("Kanishk Rawat (BCA EA) \n");
    int Marks_1, Marks_2 , Marks_3,Marks_4,Marks_5, Total , Percentage ;
    printf("Enter your marks in maths (out of 100) :-");
    scanf("%d", &Marks_1);
    printf("Enter your marks in Physics (out of 100) :-");
    scanf("\n%d", &Marks_2);
    printf("Enter your marks in Chemistry (out of 100) :-");
    scanf("\n%d", &Marks_3);
    printf("Enter your marks in Biology(out of 100) :-");
    scanf("\n%d", &Marks_4);
    printf("Enter your marks in Computer (out of 100) :-");
    scanf("\n%d", &Marks_5);
    Total = Marks_1 + Marks_2 + Marks_3  +Marks_4 +Marks_5;
    Percentage = Total / 5;
    if (Percentage>=90){
        printf("Your Grades are A ");
    
    }
    else if (Percentage>=80){
        printf("Your Grades are B ");
    
    }
    else if (Percentage>=70){
        printf("Your Grades are C");
    
    }
    else if (Percentage>=60){
        printf("Your Grades are D ");
    
    }
    
    else if (Percentage>=50){
        printf("Your Grades are E ");
    
    }
    
    else if (Percentage>=40){
        printf("Your Grades are F ");
    
    }
    
}