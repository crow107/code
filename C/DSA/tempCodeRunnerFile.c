#include<stdio.h>

int main()
{

    int i, n;      //Traversal
    int arr[10];     
    printf("\nEnter the number of elements in the array: ");
	scanf("%d",&n);
	printf("\nEnter elements of array: \n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
    printf("\n The array elements are: ");
	for(i=0;i<n;i++)
    {
		printf("\n arr[%d]= %d", i, arr[i]);
    }
     return 0;
}
