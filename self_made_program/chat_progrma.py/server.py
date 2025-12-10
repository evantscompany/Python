import socket
import threading

clients=[]

def handle_client(client,addr):
    print(f"[연결됨]{addr} 연결됨")
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            broadcast(msg,client)
        except:
            break
    print(f"[연결종료]{addr} 연결종료")
    clients.remove(client)
    client.close()

def broadcast(msg, sender):
    for client in clients:
        if clients !=sender:
            try :
                client.send(msg)
            except:
                clients.remove(client)

HOST = '0.0.0.0'
PORT = 5000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f"[서버 시작] {HOST}:{PORT}에서 대기중")

while True:
    client, addr = server.accept()
    clients.append(client)

    threading.Thread(target=handle_client,args=(client,addr),daemon=True).start()

    