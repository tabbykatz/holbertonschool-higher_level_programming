#include "lists.h"

/**
 * check_cycle - find a loop in a list
 * @list: points to beginning of list
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;
	while (tortoise && hare && hare->next)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
