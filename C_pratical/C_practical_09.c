#include <stdio.h>

struct employee{
    int Employee_Id;
    char Employee_Name[20];
    int Age;
    char Address[20];
    char Department[20];
    int Salary;
};

int main(){
    struct employee employees[10];
    for(int i = 0 ;i<10;i++){
        printf("Enter The Id of Employee - ");
        scanf("%d",&employees[i].Employee_Id);
        printf("Enter The Name of Employee - ");
        scanf("%s",&employees[i].Employee_Name);
        printf("Enter The Age - ");
        scanf("%d",&employees[i].Age);
        printf("Enter The Address - ");
        scanf("%s",&employees[i].Address);
        printf("Enter The Department - ");
        scanf("%s",&employees[i].Department);
        printf("Enter The Salary - ");
        scanf("%d",&employees[i].Salary);
    }
    for(int i = 0 ;i<10;i++){
        printf("Employee Name = %s,with id=%d,Age =%d,Address =%s,Department=%s,Salary  =%d\n",employees[i].Employee_Name,employees[i].Employee_Id,employees[i].Age,employees[i].Address,employees[i].Department,employees[i].Salary);
    }
}