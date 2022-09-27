#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome-checks if a list is palindrom
 * @head: the head of the lis
 * 
 * Return: 1 if palindrome and 0 otherwise
 * 
 */

int is_palindrome(listint_t **head)
{
    listint_t *temp = *head, *temp0 = *head;
    listb *theList, *last, *theHead = NULL, *hc;
    while(temp != NULL)
    {
        theList = (listb*)malloc(sizeof(listb));
        theList->n = temp->n;
        theList->next = NULL;
        if(theHead == NULL)
        {
            theList->prev = NULL;
            theHead = (listb*)theList;
            continue;
        }
       
        hc = (listb*)theHead;
        while(hc->next != NULL){
	  hc = (listb*)hc->next;
        }
        hc -> next = theList;
        theList -> prev = hc;
        last = theList;
         temp = temp->next;
    }
    while(temp0 != NULL){
        if(last->n == temp0->n){
            last = (listb*)last->prev;
            temp0 = temp0->next;
            continue;
        }else{
            return 0;
        }
        last = (listb*)last->prev;
        temp0 = temp0->next;
    }
    return 1;
}
