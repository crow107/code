#include <stdio.h>

struct employee
{
    int Employee_Id;
    char Employee_Name[20];
    int Age;
    char Address[20];
    char Department[20];
    int Salary;
};

int main()
{
    struct employee employees[10];
    int eid;
    for (int i = 0; i < 10; i++)
    {
        printf("-------------For Employee %d ---------\n", i + 1);
        printf("Enter The Id of Employee - ");
        scanf("%d", &employees[i].Employee_Id);
        printf("Enter The Name of Employee - ");
        scanf("%s", &employees[i].Employee_Name);
        printf("Enter The Age - ");
        scanf("%d", &employees[i].Age);
        printf("Enter The Address - ");
        scanf("%s", &employees[i].Address);
        printf("Enter The Department - ");
        scanf("%s", &employees[i].Department);
        printf("Enter The Salary - ");
        scanf("%d", &employees[i].Salary);
    }

    printf("Enter The Id of Employee -");
    scanf("%d", &eid);
    int k = 0;
    for (int i = 0; i < 10; i++)
    {
        if (eid == employees[i].Employee_Id)
        {
            printf("Employee Name = ", employees[i].Employee_Name);
            printf("Employee Age = ", employees[i].Age);
            printf("Employee Address = ", employees[i].Address);
            printf("Employee Department = ", employees[i].Department);
            printf("Employee Salary = ", employees[i].Salary);
            k = 1;
            break;
        }
    }
    if (k == 0)
    {
        printf("No One is associated with this id");
    }
}