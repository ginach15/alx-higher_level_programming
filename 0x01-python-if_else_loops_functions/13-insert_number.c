#include <stdlib.h>

#include "lists.h"

/**
 * insert_node - inserts a node into a linked list
 * @head: pointer to pointer to beginning of linked list
 * @number: integer to be entered into new node
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *temp;

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
	current = temp = *head;
	if (new->n <= current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL)
	{
		if (new->n <= current->next->n)
		{
			temp = current;
			current = current->next;
			temp->next = new;
			new->next = current;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	new->next = NULL;
	return (new);
}
