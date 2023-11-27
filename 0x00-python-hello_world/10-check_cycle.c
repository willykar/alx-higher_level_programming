#include "lists.h"
/**
 * check_cycle - A function that checks if a singly linked list has
 * a cycle in it
 * @list: A pointer to the list
 * Return: (0) if there is no cycle or
 * (1) if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p21;
	listint_t *prev;

	p21 = list;
	prev = list;
	while (list && p21 && p21->next)
	{
		list = list->next;
		p21 = p21->next->next;

		if (list == p21)
		{
			list = prev;
			prev =  p21;
			while (1)
			{
				p21 = prev;
				while (p21->next != list && p21->next != prev)
				{
					p21 = p21->next;
				}
				if (p21->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
