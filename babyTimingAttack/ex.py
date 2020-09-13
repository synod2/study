from pwn import *
import time
import string 

p = process("./main")

payload = "000000"
res = ""

for j in range(1,7) : 
    for i in string.printable :
        start = time.time()
        tmp = res+str(i)+payload[j:]
        print tmp
        p.sendlineafter(">>",tmp)
        print time.time()-start
        if time.time()-start > 0.25+0.3*j : 
            res += str(chr(ord(i)-1))
            print "find str: "+res
            break
        
# for j in range(0,10) :
#      start = time.time()
#      p.sendlineafter(">>","f1est7")
#      print time.time()-start

                
p.interactive()