# -*- coding: utf-8 -*-

import socket as socket
import threading as th
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

if (len(sys.argv) != 3):
  print("Uso Correto: script, IP, porta")
  exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])

TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP.bind((ip, port))
TCP.listen(1)
connections = []
usersConnected = []

print("Servidor está rodando em {}:{}".format(ip, port))
print("\n > Aguardando conexão...\n")


def connected():
  connection, client = TCP.accept()  
  client_name = connection.recv(1024).decode()


  if client_name != "/SAIR":
    print(" > Conexão estabelicida com", client_name)
    connections.append(connection)
    usersConnected.append(client_name)

    t = th.Thread(target=connected)
    t.start()

    message = ""
    while message != '/SAIR':
      message = connection.recv(1024).decode()      
      if message == '/USUARIOS':
        answer = 'Usuarios conectados: ' + ', '.join(usersConnected)
        print(answer)
        connection.send(answer.encode())
      else:
        answer = "[" + client_name + "]: " + message
        print(answer)

      if len(connections) == 1 and message != "/SAIR" and message != "" and message != "/USUARIOS":
        nota = " Nota: Só você está no chat. Esperando por mais clientes para iniciar o chat!\n"
        print(" > ", answer)
        
        connection.send(nota.encode())
      elif message != "/SAIR" and message != "" and message != "/USUARIOS":
        for con in connections:
          if (con != connection):
            con.send(answer.encode())

    print(" > Conexão finalizada com {}".format(client_name))
    connections.remove(connection)

    if len(connections) == 0:
      message = "close"
    connection.send(message.encode())
    _ = connection.recv(1024).decode()
    connection.close()
  else:
    print(" ╔══════════════════════════╗")
    print(" ║   SERVIDOR FORA DO AR    ║")
    print(" ╚══════════════════════════╝")
    connection.close()

t = th.Thread(target=connected)
t.start()

