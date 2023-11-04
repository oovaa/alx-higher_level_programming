#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *start = *head;
	int len = 0;
	int mid, i, j;

	if (*head == NULL)
		return (1);

	while (last)
	{
		last = last->next;
		len++;
	}
	mid = len / 2;

	int arr[len];

	for (i = 0; start; i++)
	{
		arr[i] = start->n;
		start = start->next;
	}

	j = len - 1;

	for (i = 0; i < mid; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}

	return (1);
}
