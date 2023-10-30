#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *cur = list;

	while (cur)
	{
		if (cur->n == 9999999)
			return (1);

		cur->n = 9999999;
		cur = cur->next;

	}
	return (0);
}

