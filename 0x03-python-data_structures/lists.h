#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * struct mylist - singly linked list
 * @n: integer
 * @next: points to the next node
 * @prev: points to the prev node
 *
 * Description:  nnn
 */
typedef struct mylist
{
   struct listb *prev;
   int n;
   struct listb *next;


}listb;
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
