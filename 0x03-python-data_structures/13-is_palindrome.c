#include "lists.h"
/**
 * reverse_list - reverse a linked list
 * @head: points to list
 * Return: addy of new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
/**
 * is_palindrome - tests if sll is a palindrome
 * @head: points to list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head, *one, *two;

	if (!(head && *head) || (*head)->next == NULL)
		return (1);
	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		one = tortoise;
		tortoise = tortoise->next;
	}

	tortoise = reverse_list(&tortoise);
	two = tortoise;
	hare = *head;
	while (hare && tortoise)
	{
		if (hare->n != tortoise->n)
			return (0);
		hare = hare->next;
		tortoise = tortoise->next;
	}
	tortoise = reverse_list(&two);
	one->next = tortoise;
	return (1);
}
