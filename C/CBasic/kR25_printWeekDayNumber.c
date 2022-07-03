# include <stdio.h>

void main(){
    int dayNum;
    printf("Kanishk Rawat (BCA EA) \n");
    printf("Enter the Week Number to find the day name:-");
    scanf("%d",&dayNum);
    switch (dayNum)
    {
    case 1 : printf("Monday");
        break;
    case 2 : printf("Tuesday");
        break;
    case 3 : printf("Wednesday");
        break;
    case 4 : printf("Thursday");
        break;
    case 5 : printf("Friday");
        break;
    case 6 : printf("Saturday");
        break;
    case 7 : printf("Sunday");
        break;
    
    default:
        printf("week only have 7 days ^_^ ");
        break;
    }
}