#include <stdio.h>
int main()
{
    int r, c, a[100][100], b[100][100], sum[100][100], mul[100][100],transpose[100][100];
    printf("Enter the number of rows (between 1 and 100): ");
    scanf("%d", &r);
    printf("Enter the number of columns (between 1 and 100): ");
    scanf("%d", &c);
    printf("\nEnter elements of 1st matrix:\n");
    for (int i = 0; i < r;i++)
        for (int j = 0; j < c;j++)
        {
            printf("Enter element a%d%d: ", i + 1, j + 1);
            scanf("%d", &a[i][j]);
        }
    printf("Enter elements of 2nd matrix:\n");
    for (int i = 0; i < r;i++)
        for (int j = 0; j < c; ++j)
        {
            printf("Enter element b%d%d: ", i + 1, j + 1);
            scanf("%d", &b[i][j]);
        }
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
        {
            sum[i][j] = a[i][j] + b[i][j];
        }
    printf("\nSum of two matrices: \n");
    for (int i = 0; i < r; i++)
        for ( int j = 0; j < c;j++)
        {
            printf("%d\t", sum[i][j]);
            if (j == c - 1)
            {
                printf("\n");
            }
        }

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            mul[i][j] = 0;
            for (int k = 0; k < c; k++)
            {
                mul[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    printf("\nProduct of two matrices: \n");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%d\t", mul[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < r;i++)
        for (int j = 0; j < c; j++)
        {
            transpose[j][i] = a[i][j];
        }
    printf("\n Transpose of matrices A: \n");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%d\t", transpose[i][j]);
        }
        printf("\n");
    }



}

