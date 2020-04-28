#include "lists.h"

/**
 * check_cycle - check for a loop.
 * @list: list containing nodes.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *check1 = list;
	listint_t *check2 = list;

	if (list == NULL)
	{
		return (0);
	}
	while (check1 && check1->next)
	{
		check1 = check1->next->next; /*Advances all nodes if it finds a loop */
		check2 = check2->next; /*Advanced by a single node */

	if (check2 == check1)
		return (1);

	}

	return (0);

}
