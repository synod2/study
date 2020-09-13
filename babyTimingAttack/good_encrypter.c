#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <memory.h>
#include <stdio_ext.h>

unsigned char encrypt(char x);

char pwd[] = "******";    // 6 printable chars! 0-9, a-z
unsigned int key;   // random key

int main() {
    unsigned char input[7] = {0, };
    int fd = open("/dev/urandom", 0);
    int isCorrect = 0;

    setvbuf(stdout, 0LL, 2, 0LL);

    if (fd < 0) {
        perror("cannot open urandom");
        exit(-1);
    }

    if (read(fd, &key, 4) < 0) {    // get random key
        perror("cannot read fd");
        exit(-1);
    }
    close(fd);
    
    printf("Input 6-char password!\n");

    while (1) {
        memset(&input, 0x00, 7);    //clear stack
        __fpurge(stdin);    // clear stdin buffer
        printf(">> ");
        fgets(input, 7, stdin);
        if (strlen(input) != 6 ) {   //input 6 printable chars
            printf("Please input 6 chars %s\n", input);
            exit(-1);
        }
        
        for (int i = 0; i < strlen(pwd); i++) { //strlen(pwd) == 6
            if (encrypt(pwd[i]) != encrypt(input[i]))
                break;
            if (i == strlen(pwd) - 1)
                isCorrect = 1;
        }
        
        if (isCorrect)
            break;
    }

    printf("You broke my password!\n");
    getchar();
    return 0;
}

unsigned char encrypt(char x) {     // encrypt argument x
    unsigned char ret = 0x00;

    for (unsigned int i = 0; i < 0xBAD; i++)
        for (unsigned int j = 0; j < 0x2000; j++)
            for (unsigned int k = 0; k < 4; k++)
                ret = x ^ (key >> (8 * k));
    return ret;
}

