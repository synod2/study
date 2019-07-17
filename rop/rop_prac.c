#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc -mpreferred-stack-boundary=2 -m32 -fno-stack-protector rop_prac.c -o rop_prac

char param[16];

int main()
{
	char buf[16];
	printf("system call's addr : %p \n",*system);
	printf("overflow now!>>");
	read(0,buf,120); 
	return 0;
}