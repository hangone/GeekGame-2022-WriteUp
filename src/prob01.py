from pwn import *
import gmpy2

def bili():
    p.sendline(bytes("418645518", encoding = "utf-8"))

def isprime(prime):
    pr = gmpy2.next_prime(prime)
    p.sendline(bytes(str(pr), encoding="utf-8"))

def android():
    p.sendline(bytes("cn.edu.pku.pkurunner", encoding="utf-8"))

def webp():
    p.sendline(bytes("65", encoding="utf-8"))

def android():
    p.sendline(bytes("cn.edu.pku.pkurunner", encoding="utf-8"))

def doi():
    p.sendline(bytes("10.14778/2002974.2002976", encoding="utf-8"))

def ctf():
    p.sendline(bytes("ctf.xn--4gqwbu44czhc7w9a66k.com", encoding="utf-8"))

def mac():
    p.sendline(bytes("80304", encoding="utf-8"))

def ele(level):
    p.sendline(bytes(str(300+int(level**1.5)*100), encoding="utf-8"))

def solve():
    r = p.recv()
    print(r.decode())
    if bytes("错误", encoding="utf-8") in r:
        return
    elif b'flag' in r:
        exit()
    elif b'av' in r:
        bili()
    elif b'Android' in r:
        android()
    elif b'WebP' in r:
        webp()
    elif bytes("质数", encoding="utf-8") in r:
        isprime(int(r.decode().split(' ')[3]))
    elif b'DOI' in r:
        doi()
    elif b'ctf' in r:
        ctf()
    elif b'MAC' in r:
        mac()
    elif bytes("电子游戏概论", encoding="utf-8") in r:
        ele(int(r.decode().split(' ')[6]))
    solve()

p = remote("prob01.geekgame.pku.edu.cn", 10001)
token = "115:MEQCIHO6hP4fDSzfjEmDA99kA-hNlx8PQBXSgETB-Tnd7GvYAiBNvLnTTT2hJ6MWRUq9LVmCA1XIMVVleSDdud8TFk3gWA=="
p.recv()
p.sendline(bytes(token, encoding="utf-8"))
p.recv()
p.sendline(bytes("急急急", encoding="utf-8"))
solve()
p.interactive()