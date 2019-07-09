#include <stdio.h>
#include <stdlib.h>
// gcc -mpreferred-stack-boundary=2 -no-pie -m32 -fno-stack-protector rtl_prac1.c -o rtl_prac

char param[16];

int main()
{
	char buf[16];
	printf("system call's addr : %p \ninput parameter!>>",*system);
	gets(param);
	printf("overflow now!>>");
	gets(buf); 
	return 0;
}