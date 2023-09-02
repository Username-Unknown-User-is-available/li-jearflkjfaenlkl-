import socket
from threading import Thread

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress="127.0.0.1"
port=8000

server.bind((ipaddress, port))
server.listen()
listofclients=[]
nicknames=[]

print("Server is Running. :)")

def clientThread(connection, adress):
    connection.send("Wellcome to this chatroom.".encode("utf-8"))
    while True:
        try:
            message=connection.recv(2048).decode("utf-8")
            if message:
                print
                broadcast(message, connection)
            else:
                remove(connection)
                remove(nickname)
        except:
            continue
def broadcast(message, connection):
    for client in listofclients:
        if client!=connection:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)

def remove(connection):
    if connection in listofclients:
        listofclients.remove(connection)

def removenickname(nickname):
    if nickname in nicknames:
        nicknames.remove(nickname)

while True:
    connection,adress=server.accept()
    connection.send("NICKNAME".encode("utf-8"))
    nickname=connection.recv(2048).decode("utf-8")
    listofclients.append(connection)
    nicknames.append(nickname)
    message="{} joined".format(nickname)
    print(message)
    broadcast(message, connection)

    newthread=Thread(target=clientThread, args=(connection, nickname))
    newthread.start()