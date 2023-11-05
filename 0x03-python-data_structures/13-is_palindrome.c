#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if (slow->n != prev->n)
			return (0);

		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
