#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - A function that adds a new node at
the beginning of a listint_t list
*@head_butt: The head of listint_t
*@n: number of type integer to add in listint_t list
*Return: (address of the new element, or NULL if it fails)
*/
listint_t *add_nodeint(listint_t **head_butt, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head_butt;
	*head_butt = new;
	return (new);
}
/**
*is_palindrome - A function that identifies if a syngle
linked list is a palindrome
*@head_butt: The head of listint_t
*Return:(1) if it is palindrome or (0)
*/
int is_palindrome(listint_t **head_but)
{
	listint_t *head2 = *head_but;
	listint_t *aux = NULL, *aux2 = NULL;

	if (*head_but == NULL || head2->next == NULL)
		return (1);
	while (head2 != NULL)
	{
		add_nodeint(&aux, head2->n);
		head2 = head2->next;
	}
	aux2 = aux;
	while (*head_but != NULL)
	{
		if ((*head_but)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head_but = (*head_but)->next;
		aux2 = aux2->next;
	}
	free_listint(aux);
	return (1);
}
