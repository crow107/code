#include<stdio.h>
#include<stdlib.h>
void create();
void insertion_at_sorted_list();
struct node{
	int data;
	struct node *next;
};
struct node *head,*temp;
int main()
{
	printf("Enter sorted list in the linked list\n");
	create();
	insertion_at_sorted_list();
}
void create()
{
	struct node *newnode;
	head=NULL;
	int n,i;
	printf("enter no of nodes\n");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		newnode=(struct node*)malloc(sizeof(struct node));
		printf("enter data\n");
		scanf("%d",&newnode->data);
		newnode->next=NULL;
		if(head==NULL)
		{
			temp=head=newnode;
		}
		else
		{
			temp->next=newnode;
			temp=temp->next;
		}
	}
	temp=head;
	printf("your sorted list is : \n");
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp=temp->next;
	}
}
void insertion_at_sorted_list()
{
	struct node *new;
    struct node *next1;
	int item;
	new=(struct node*)malloc(sizeof(struct node));
	printf("enter item to insert\n");
	scanf("%d",&new->data);
	item=new->data;
	if((head==NULL) || (item < head->data))
	printf("cant be inserted\n");
	else
	{   
        next1=NULL;
		temp=head;
		while(item >temp->data)
		{   next1 = temp;
			temp=temp->next;
		}
		new->next=next1->next;
		next1->next=new;
		
		temp=head;
		printf("List after insertion is : \n");
		while(temp!=NULL)
		{
		
			printf("%d ",temp->data);
			temp=temp->next;
		}
	}
	
	
}

