from socket import *
import random#ALICE
HOST=''
PORT=8090
sockobj=socket(AF_INET,SOCK_STREAM)
sockobj.bind((HOST,PORT))
sockobj.listen(5)
def similar():
    while True:
        n=random.randint(1,100)
        d = 2
        if n % d != 0:
            break
    return n
p=similar()
q=0

while True:
    connection,adress=sockobj.accept()
    print('Connected to:',adress)
    while True:
        data=connection.recv(1024)#1st recv is q
        if not data:break
        q=int(data)

        connection.send(str.encode(str(p)))#1st send is p
        akey=random.randint(1,10)

        data=connection.recv(1024)#2nd recv is new privatekey

        bkey=int(data)
        aliceprivatekey=(q**bkey)%p#calculate privatekey
        connection.send(str.encode(str(akey)))#2nd send is old privatekey
        aliceprivetekey=(aliceprivatekey**akey)%p#common key
        print('common key',aliceprivetekey)
    connection.close()
