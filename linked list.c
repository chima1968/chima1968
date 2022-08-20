#include<stdio.h> // define the header file
#include<stdlib.h>

struct node{
    /*this structure defines the node*/
    int data;
    struct node *link;

};

void display(struct node *temp){
    /*this function prints out the linked list*/
    while (temp!=0){
        printf("%d",temp->data);
        temp=temp->data;
    
    }



}
     
int main()   // define the main function  
{    
    
    struct node* head=(struct node*)malloc(sizeof(struct node*));
    head->data=45;
    head->link=NULL;
    
    
    struct node* next=(struct node*)malloc(sizeof(struct node*));
    next->data=90;
    next->link=NULL;
    head->link=next
    
    struct node* current=(struct node*)malloc(sizeof(struct node*));
    currect->data=23;
    current->link=NULL;
    next->link=current
    
        
     display(head);
    
    
    
    return 0;
}  
