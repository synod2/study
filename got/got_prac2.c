#include <stdio.h>
//gcc -mpreferred-stack-boundary=2 -z norelro -m32 got_prac2.c -o got_prac2

void shell(){
	
	printf("yes! you write rightly!\n");
	system("/bin/sh");
	
}


int main()
{
	int *addr;
	
	fflush(stdin);
	
	printf("shell func's pointer : %p\n",*shell);
	
	printf("place to write : ");
	gets(&addr);
	
	fflush(stdin);
	printf("address to write : ");
	gets(addr);
	
	fflush(stdin);
	printf("did you think writing goes right?\n");
	return 0;
	
}
