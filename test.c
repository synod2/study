#include<stdio.h>
//gcc -mpreferred-stack-boundary=2 -z norelro -m32 got_prac2.c -o got_prac2
void func1(){
        printf("func 1 called!\n");
}

void func2(){
        printf("func 2 called!\n");
}

int main()
{
        printf("CAT-Security\n");
        printf("Welcome To the Summer-study\n");
        printf("Let's burn~\n");
        func1();
        func2();
}