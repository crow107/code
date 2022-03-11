#include <stdio.h>
int main()
{
    int a = 1;
    while (a == 1)
    {
        int num, operation;
        printf("Enter the Number :-");
        scanf("%d", &num);
        printf("1.Armstrong Numer\n2.Prime Number Between\n3.Reverse\n4.Exit\n:-");
        scanf("%d", &operation);
        if (operation == 1)
        {
            int temp, sum = 0, r;
            temp = num;
            while (temp > 0)
            {
                r = temp % 10;
                sum = sum + (r * r * r);
                temp = temp / 10;
            }
            if (num == sum)
            {
                printf("armstrong  number \n");
            }
            else
            {
                printf("not armstrong number\n");
            }
        }
        else if (operation == 2)
        {
            int flag, temp;
            temp = num;
            for (int i = 1; i < temp; i++)
            {
                flag = 0;
                for (int j = 2; j <= i / 2; j++)
                {
                    if (i % j == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0)
                {
                    printf("%d ", i);
                }
            }
            printf("\n");
        }
        else if (operation == 3)
        {
            int temp, r, newnum = 0;
            temp = num;
            while (temp != 0)
            {
                r = temp % 10;
                newnum = newnum * 10 + r;
                temp /= 10;
            }
            printf("Reverse of %d is %d \n", num, newnum);
        }
        else if (operation == 4)
        {
            break;
        }
        else
        {
            printf("Hello");
        }
    }
}