#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * reverse_listint - A function that reverses a linked list
 * @head: The pointer to the first node
 *
 * Return: (A pointer to the first node in the new list)
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}
/**
*is_palindrome - A function that identifies if a syngle
linked list is a palindrome
*@head_butt: The head of listint_t
*Return:(1) if it is palindrome or (0)
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fas = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fas = fas->next->next;
		if (!fas)
		{
			dup = slow->next;
			break;
		}
		if (!fas->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
