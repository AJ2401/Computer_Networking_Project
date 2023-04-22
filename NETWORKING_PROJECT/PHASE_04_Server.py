import socket
from random import*
import os
from os import system

os.system('clear')
print("My IP : \n")
print('-----------------------------------------------------------------------------\n')
os.system('ifconfig | tail -11 | head -2 | tail -1')
print('\n-----------------------------------------------------------------------------\n')
print("\n\n\n")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True: 
	l=int(input('Enter Lower Limit :  \n'))
	if l>5 :
		break
while True:
	u=int(input('Enter Upper Limit : \n'))
	if u>25:
		break;

r=1000*(u-l)+l


print("PORT" + str(r))
serversocket.bind(('192.168.1.7',r))
serversocket.listen(5) # become a server socket, maximum 5 connections
connected = False
file_sent = False

while True:
	connection,address = serversocket.accept()
	connected=Truekeys()
	buff = connection.recv(64).decode()
	p='Start'
	connection.send(p.encode())
	buf = connection.recv(64).decode()
	print("Client is Requesting for this File : "+buf)
	
	try:
		file = open('source_folder/'+buf,'r')
		file_contents = file.read()
		#print(file_contents)
		connection.send(file_contents.encode())
		file_sent = True
		pass
	except:
		message="file doesnt exist"
		connection.send(message.encode())
		reply=connection.recv(64).decode()
		if reply=='yes':
			f=open("source_folder/"+buf,"w+")
			message2="file created"
			connection.send(message2.encode())
			name=connection.recv(64).decode()
			branch=connection.recv(64).decode()
			sec=connection.recv(64).decode()
			hostel=connection.recv(64).decode()
			f.write(name)
			f.write(branch)
			f.write(sec)
			f.write(hostel)	
			f.close()
			f=open("source_folder/"+buf,"r")
			print(f.read())
			file_sent = True
		else:
			break
	
	buf = connection.recv(64).decode()
	if connected == True and file_sent == True and buf == 'done':
		print('Client Request is Fulfilled and getting Closed !\n\n')
		break
print("Server is Closing !\n\n")