#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: head of Linked List to insert
 * @number: Number to Insert
 * Return: Node inserted or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *node = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (node->next)
	{
		if (node->n >= number)
		{
			new->next = node;
			*head = new;
			return (new);
		}
		if ((number >= node->n) && (node->next == NULL))
		{
			new->next = NULL;
			new->next = node->next;
			return (new);
		}
		if ((number >= node->n) && (number <= node->next->n))
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}
	return (NULL);
}
