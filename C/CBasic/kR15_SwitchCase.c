# include <stdio.h>

void main(){
    int num;
    printf("Enter the numeber:");
    scanf("%d",&num);
    switch(num){
        case 1: 
        printf("monday");
        break;
        case 2:
        printf("Tuesday");
        break;
        case 3:
        printf("Wednesday");
        break;
        case 4: 
        printf("Thusday");
        break;
        case 5:
        printf("Friday");
        break;
        case 6:
        printf("Saturday");
        break;
        case 7:
        printf("Sunday");
        break;
        default:
        printf("OK BYe");
        break;
    }
}