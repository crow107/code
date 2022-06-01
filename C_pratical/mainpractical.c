#include <stdio.h>

struct student
{
    int student_Id;
    char student_Name[20];
    int Age;
    char Address[20];
    char Department[20];
    int Course;
};

int main()
{
    struct student students[10];
    int eid;
    for (int i = 0; i < 10; i++)
    {
        printf("-------------For student %d ---------\n", i + 1);
        printf("Enter The Id of student - ");
        scanf("%d", &students[i].student_Id);
        printf("Enter The Name of student - ");
        scanf("%s", &students[i].student_Name);
        printf("Enter The Age - ");
        scanf("%d", &students[i].Age);
        printf("Enter The Address - ");
        scanf("%s", &students[i].Address);
        printf("Enter The Department - ");
        scanf("%s", &students[i].Department);
        printf("Enter The Course - ");
        scanf("%d", &students[i].Course);
    }

    printf("Enter The Id of student -");
    scanf("%d", &eid);
    int k = 0;
    for (int i = 0; i < 10; i++)
    {
        if (eid == students[i].student_Id)
        {
            printf("student Name = ", students[i].student_Name);
            printf("student Age = ", students[i].Age);
            printf("student Address = ", students[i].Address);
            printf("student Department = ", students[i].Department);
            printf("student Course = ", students[i].Course);
            k = 1;
            break;
        }
    }
    if (k == 0)
    {
        printf("No One is associated with this id");
    }
}