#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

// gcc -mpreferred-stack-boundary=2 -no-pie -z norelro -m32 fsb_prac.c -o fsb_prac

int main()
{
    srand(time(NULL));
    int random = rand()%100;
    char buf[16];
    int ans = 0;
    
    printf("what is your name? \n");
    read(0,buf,16);
    printf("hello, \n");
    printf(buf);
    printf("\nwhat is secret number?\n> ");
    scanf("%d",&ans);
    
    if (ans == random)
        printf("correct!\n");
    else 
        printf("wrong!\n");
}