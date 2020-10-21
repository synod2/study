#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

// gcc -mpreferred-stack-boundary=2 -no-pie -z norelro -m32 fsb_32.c -o fsb_32

int target = 0 ;
void (*func)() ;

void shell(){
    printf("you got the shell..")
    system("/bin/sh");
}

void show(){
	printf("\nvalue is : %d , right?\n",target);
}


int main()
{
    srand(time(NULL));
    char buf[120] = {0,};
	
	target = rand();
	func =  show;
	printf("origin value is : %d ,  addr is : %x \n",target,&target);
	printf("fsb now!>>\n");
	read(0,buf,100); 
	printf(buf);
    func();
	return 0;
}