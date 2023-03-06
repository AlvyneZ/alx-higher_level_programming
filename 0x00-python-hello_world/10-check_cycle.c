#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

#define LIST_CHCK_CCL_BUFFER_SIZE 256

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to head of linked list
 *
 * Return: 1 if present, 0 if absent
 */
int check_cycle(listint_t *list)
{
	int buf_sz = 0, buf_cnt = 0, cnt;
	listint_t **tmp = NULL,  **buf = NULL;

	while (list != NULL)
	{
		if (buf_cnt == buf_sz)
		{
			buf_sz += LIST_CHCK_CCL_BUFFER_SIZE;
			tmp = buf;
			buf = malloc(sizeof(listint_t *) * buf_sz);
			if (buf == NULL)
			{
				if (tmp != NULL)
					free(tmp);
				return (-1);
			}
		}
		for (cnt = 0; cnt < buf_cnt; cnt++)
		{
			if (tmp != NULL)
				buf[cnt] = tmp[cnt];
			if (list == buf[cnt])
			{
				if (tmp != NULL)
					free(tmp);
				free(buf);
				return (1);
			}
		}
		if (tmp != NULL)
		{
			free(tmp);
			tmp = NULL;
		}
		buf[buf_cnt] = list;
		buf_cnt++;
		list = list->next;
	}
	free(buf);
	return (0);
}
