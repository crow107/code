#include <stdio.h>
#include <stdlib.h>

struct node
{
    int info;
    struct node *link;
};
struct node *insertNode(int info,struct node *link){
    struct node *ptr = (struct node *) malloc(sizeof(struct node));
    link->info = info;
    link->link = ptr;
    return ptr;
}
void EndNode(int info,struct node *link){
    link->info = info;
    link->link = NULL;
}

void display(struct node *start){
    struct node *ptr =start;
    printf("\n");
    while (ptr != NULL)
    {
        printf(" [%d | %p] ", ptr->info, ptr->link);
        ptr = ptr->link;
    }
}


int main(){
    struct node *start = (struct node *) malloc (sizeof(struct node));
    struct node *Fnode = insertNode(5,start);   // link = start , info = 5 ptr =2
    struct node *Snode = insertNode(6,Fnode);
    struct node *Tnode = insertNode(7,Snode);
    EndNode(8,Tnode);
    display(start);

}