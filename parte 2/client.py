# -*- coding: utf-8 -*-

import socket as sk
import threading as th
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')


# ip = str(sys.argv[1])
# port = int(sys.argv[2])
print("Bem vindo! Para entrar no chat digite:\n /ENTRAR ip porta")
print("Ex.: /ENTRAR localhost 3000")
command = ""
while command != "/ENTRAR":
  userInput = input("")
  userWords = userInput.split()
  command = userWords[0]
  ip = userWords[1]
  port = int(userWords[2])
  if (command != "/ENTRAR"):
    print("Comando inválido, tente novamente.")

def recv_server_msg(sock):
  stop = False
  while not stop:
    message = sock.recv(1024).decode()
    if message == "/SAIR":
      sock.send("".encode())
      sock.close()
      stop = True
    elif message == "close":
      sock.close()
      TCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
      TCP.connect((ip, port))
      TCP.send("/SAIR".encode())
      TCP.close()
      stop = True
    elif len(message.split()) > 0 and message.split()[1] != "/SAIR":
      print(message, "\n > ", end="")
 
try:
  TCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
  TCP.connect((ip, port))

  t = th.Thread(target=recv_server_msg, args=(TCP, ))
  t.start()

  print("\n > Digite seu nome: ", end="")
  message = input("")
  while message == "/SAIR" or message == "/USUARIOS" or not message:
    print(" > NOME INVÁLIDO!")
    print(" > Digite seu nome: ", end="")
    message = input("")

  print("\n ╔═════════════════════════════╗")
  print(" ║     ENVIE SUA messagem      ║")
  print(" ║ Para ver os usuários online ║")
  print(" ║      digite: /USUARIOS      ║")
  print(" ║   Para sair digite: /SAIR   ║")
  print(" ╚═════════════════════════════╝\n")

  while message != '/SAIR':
    TCP.send(message.encode())
    message = input(" > ")

  TCP.send(message.encode())
  print("\n ╔═════════════════════════════╗")
  print(" ║  DESCONECTADO DO SERVIDOR   ║")
  print(" ╚═════════════════════════════╝")
  exit()
    
except ConnectionRefusedError:
  print("\n > Servidor fora do ar!")