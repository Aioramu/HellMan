import sys,random#BOB
from socket import *
sHOST='localhost'
sPORT=8090
def similar():
    while True:
        n=random.randint(1,100)
        d = 2
        if n % d != 0:
            break
    return n
p=0
q=similar()
sockobj=socket(AF_INET,SOCK_STREAM)
sockobj.connect((sHOST,sPORT))

sockobj.send(str.encode(str(q)))#1st send is q
data=sockobj.recv(1024)#1st recv is p
p=int(data)
bkey=random.randint(1,10)
sockobj.send(str.encode(str(bkey)))#2nd send is privatekey of bob
data=sockobj.recv(1024)#2nd recv is privatekey of alice
akey=int(data)
bobprivetekey=(q**akey)%p
bobprivetekey=(bobprivetekey**bkey)%p
print('common key:',bobprivetekey)
sockobj.close()
