import socket
from random import*
import os
import sys
from os import system

os.system('clear')
print('My IP : \n')
print('-------------------------------------------------------------------------- \n')
os.system('ifconfig | tail -11 | head -2 | tail -1')
print("\n")
print('-------------------------------------------------------------------------- \n')
max=1024

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

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=input("Enter the Ip address to Connect : \n\n")
#'192.168.1.9'
clientsocket.connect((ip, r))
while True:
	reg=input('\nEnter The Registration Number : \n\n')
	if len(reg)==9:
		break;
#reg=input('\nEnter The Registration Number : \n\n')
print('Sending '+ reg +' to Server')
clientsocket.send(reg.encode())

connected = False
filename = reg+'.txt'

# listen for ack
while True:
	buf = clientsocket.recv(64).decode()
	if buf == 'Start':
		# successfully connected
		connected = True
		# send the name of the file being requested
		print('Requesting '+filename+' File From SERVER !!\n\n')
		clientsocket.send(filename.encode())
	if connected == True:
		# receive the contents of the file
		buf = clientsocket.recv(max).decode()
		if buf=='file doesnt exist':
			opt=input("Enter YES to Create the File "+filename+" or NO to Not Create the File "+filename+": \n")
			if opt=="no":
				quit()
				break
			else:
				clientsocket.send(opt.encode())
				b=clientsocket.recv(64).decode()
				print("\n"+b+"\n")
				name=input('Enter the Name : \n')
				name='Name : '+name+'\n'
				clientsocket.send(name.encode())
				branch=input('Enter the Branch : \n')
				branch='Branch : '+branch+'\n'
				clientsocket.send(branch.encode())
				section=input('Enter the Section : \n')
				section='Section : '+section+'\n'
				clientsocket.send(section.encode())
				hostel=input('Enter the Hostel : \n')
				hostel='Hostel : '+hostel+'\n'
				clientsocket.send(hostel.encode())
				print("\nYour Details are Updated in the File !!\n")
				break
				exit()
		else:
			print ('File Received From Server')
			file_contents = buf
			#print(filename)
			filename=str(filename);
			file = open('destination_folder/'+filename, 'w+')
			file.write(file_contents)
			print('\nFILE RECEIVED \n')
			'''f = open('destination_folder/'+filename, 'r')
			print(f.read())
			#os.system('cat destination_folder/'+filename)'''
			file.close()
			data1='done'
			clientsocket.send(data1.encode())
			os.system('cat destination_folder/'+filename)
			print("\n\n")
			print('File Saved in Destination Folder')
			print('Sending Ack Back To Server')
			print('send done to server')
			break