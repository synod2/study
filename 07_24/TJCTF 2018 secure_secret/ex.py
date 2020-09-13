#! -*- coding:utf-8 -*-

from pwn import * 

p = process("./secure_secret")

# 프로그램 시작 시 , 패스워드를 입력하고 그 다음 메시지를 입력한다 . 
# 총 두번의 입력인데 이는 set_message 함수와 get_message 함수에서 이뤄진다. 