# include <stdio.h>
# include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *head ;
struct node *second;
struct node *third;



int main(){

    head = (struct node *) malloc(sizeof(struct node));
    second = (struct node *) malloc(sizeof(struct node));
    third = (struct node *) malloc(sizeof(struct node));


    head->data = 7;
    head->next = second;

    second->data = 10;
    second->next = third;

    third->data = 11;
    third->next =NULL;



    struct node *ptr = head;
    printf("\n[");
    while (ptr != NULL)
    {
        printf(" [%d|%p] ", ptr->data, ptr->next);
        ptr = ptr->next;
    }
    printf(" ]");
    
}