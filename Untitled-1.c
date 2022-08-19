#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *link;


};
int main(){
    struct node *temp ,*ptr;
    int start;

    printf("enter the data value for the node:");
    scanf("%d",&temp->data);
    temp->link=NULL;

    if (start==NULL){
        start=temp;
    }else{
        ptr=start;
        while (ptr->link!=NULL){
            ptr=ptr->link;
        }
        ptr->link=temp;
    }







    return 0;
}