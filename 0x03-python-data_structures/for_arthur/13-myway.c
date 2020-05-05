#include "lists.h"

/**
 * reverse_listint - reverse a list
 * @head: points to start of list
 * Return: pointer to beginning of reversed list
 */
listint_t *reverse_listint(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;


	while (head)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	head = prev;
	return (head);
}
listint_t *copy_list(listint_t *head)
{
	listint_t *new;
	listint_t *temp = malloc(sizeof(listint_t));
	
	new = temp;
	while (head)
	{
		temp->n = head->n;
		temp->next = head->next;
		temp = temp->next;
		head = head->next;
	}
	return (new);
}
int is_palindrome(listint_t **head)
{
	listint_t *location = *head;
	listint_t *reversed = reverse_listint(copy_list(location));
	
	while (location)
	{
		printf("%d : %d\n", location->n, reversed->n);
		if (location->n == reversed->n)
		{
			location = location->next;
			reversed = reversed->next;
		}
		else
			return (0);
	}
	return (1);
}


