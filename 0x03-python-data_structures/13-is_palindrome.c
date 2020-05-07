#include "lists.h"


/**
 *
 *
 *
 *
 */

listint_t *reverse_list(listint_t **h)
{
	listint_t *prev = NULL, *node = *h;
	listint_t *next;

	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	(*h) = prev;
	return (*h);
}



/**
 *
 *
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *temp = *head;

	if (!*head)
	    return (1);

	while (temp->next && temp->next->next)
	{
		node = node->next;
		temp = temp->next->next;
	}
	node = reverse_list(&node);

	temp = *head;
	while (node && temp)
	{
		if (node->n != temp->n)
			return (0);
		node = node->next;
		temp = temp->next;
	}
	return (1);
}
