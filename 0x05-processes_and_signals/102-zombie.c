/*
 * File: 102-zombie.c
 * Author: abdelouali youssef
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite loop.
 *
 * Return: Always returns 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	pid_t pid;
	int x;

	for (x = 0; x < 5; x++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
		{
			perror("fork");
			return (1);
		}
	}

	infinite_while();

	return (0);
}
