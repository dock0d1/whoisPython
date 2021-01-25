#!/usr/share/python
import socket,sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send(sys.argv[1]+"\r\n")
resposta = s.recv(1024).split()
whois = resposta[19]
s.close()
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois,43))
s1.send(sys.argv[1]+"\r\n")
resp = s1.recv(1024)
print resp