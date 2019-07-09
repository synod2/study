#include <stdio.h>
#include <stdlib.h>

// gcc -mpreferred-stack-boundary=2 -no-pie -m32 -fno-stack-protector rtl_chain.c -o rtl_chain

char param[16];

int main()
{
	char buf[16];
	printf("system call's addr : %p \n",*system);
	printf("overflow now!>>");
	gets(buf); 
	return 0;
}