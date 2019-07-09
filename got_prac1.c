#include <stdio.h>
//gcc -mpreferred-stack-boundary=2 -no-pie -z norelro -m32 got_prac1.c -o got_prac1

void shell(){
	
	printf("yes! you write rightly!\n");
	system("/bin/sh");
	
}


int main()
{
	int *addr;
	
	fflush(stdin);
	
	printf("place to write : ");
	gets(&addr);
	
	fflush(stdin);
	printf("address to write : ");
	gets(addr);
	
	fflush(stdin);
	printf("did you think writing goes right?\n");
	return 0;
	
}
