#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node into a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *previous;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else if (number < current->n)
	{
		*head = new;
		new->next = current;
	}
	else
	{
		do {
			previous = current;
			current = current->next;
		} while ((current != NULL) && (number > current->n));
		previous->next = new;
		new->next = current;
	}

	return (new);
}