// write a program to convert temperature from Celsius to Fahrenheit by taking input from the user
# include <stdio.h>
void main(){
    float temp_C;
    float temp_F;
    printf("Enter the temprature in Celsius :- ");
    scanf("%f",&temp_C);
    temp_F = (temp_C * 9/5) + 32;

    printf("The Temprature in fahrenheit :- %0.2f ", temp_F);

}   