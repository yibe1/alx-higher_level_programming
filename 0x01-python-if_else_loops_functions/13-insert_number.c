#include<stdlib.h>
#include "lists.h"
/**
 *insert_node-inserts a value at sorted list of numbers
 *@head: the pointer to the pointer of the head nod of the list
 *@number: the number to be inserted
 *
 */
listint_t *insert_node(listint_t **head, int number){

listint_t *v = (listint_t*)malloc(sizeof(listint_t));
listint_t *prevNode, *currentNode;
currentNode = *head;

int num;
while(currentNode != NULL){

    if(currentNode->n > number){
        prevNode->next = v;
        v->n = number;
        v->next = currentNode;
        return &(*v);
    }
    prevNode = currentNode;
    currentNode = currentNode->next;
}
return NULL;

}
