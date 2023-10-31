#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly-linked list.
* @head: A pointer the head of the linked list.
* @number: The number to insert.
* Author - Tolulope Fakunle
* Return: If the function fails - NULL.
*         Otherwise - a pointer to the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *cur, *new;


if (head == NULL)
	{
		return (NULL);
	}

	cur = *head;
	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (cur == NULL || cur->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}


	while (cur->next != NULL && cur->next->n < number)
	{
		cur = cur->next;
	}
	
		new->next = cur->next;
		cur->next = new;

	return (new);
}
