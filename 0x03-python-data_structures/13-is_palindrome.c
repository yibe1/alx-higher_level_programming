#include <stdlib.h>
#include <stdio.h>
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
    struct mylist *theList = NULL, *last = NULL, *theHead = NULL;
    while (temp != NULL)
    {
      theList = (struct mylist *) malloc(sizeof(struct mylist));
      theList->n = temp->n;
      theList->next = NULL;
      if (theHead == NULL)
	{
	  theList->prev = NULL;
	  theHead = theList;
	  continue;
	}

      struct mylist *hc = theHead;
      while (hc->next != NULL)
	hc = hc->next;
      hc->next = theList;
      theList->prev = hc;
      last = theList;
      temp = temp->next;
    }
    while (temp0 != NULL)
      {
	if (last->n == temp0->n)
	  {
	    last = last->prev;
	    temp0 = temp0->next;
	    continue;
	  }
	else
	  {
	    return (0);
	  }
	last = last->prev;
	temp0 = temp0->next;
      }
    return (1);
}
