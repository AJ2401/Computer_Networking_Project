import random
import ipaddress
from colorama import Fore, Back, Style
def application_layer(msg):
	print(Fore.CYAN+'\n\n\n------------------APPLICATION LAYER----------------------\n\n\n')
	msg =' (APPLICATION) - ' + msg
	print(Fore.GREEN+'\t'+msg+'\t')
	#print(,"\n")
	presentation_layer(msg)
	return

def presentation_layer(msg):
	# choose a protocol (telnet)
	print(Fore.RED+'\n\n\n------------------PRESENTATION LAYER----------------------\n\n\n')
	pres_header = ' (PRESENTATION TELNET) - '
	msg = pres_header + msg
	print(Fore.GREEN+'\t'+msg+'\t')
	#print("\n")
	session_layer(msg)
	return

def session_layer(msg):
	# choose a protocol like remote procedure protocols helps in connection loss
	print(Fore.RED+'\n\n\n------------------SESSION LAYER----------------------\n\n\n')
	sesh_header = ' (SESSION RPC) - '
	msg = sesh_header + msg
	print(Fore.GREEN+'\t'+msg+'\t')
	transport_layer(msg)
	return

def transport_layer(msg):
	# assume port 20 (00010100)
	print(Fore.RED+'\n\n\n------------------TRANSPORT LAYER----------------------\n\n\n')
	port=(int)(input(Fore.WHITE+"\nEnter the Port Number : \n"))
	p='{0:08b}'.format(port)
	tr_header = "\n(" +str(p)+ ") "+ ' TRANSPORT - '
	msg = tr_header + msg
	print(Fore.GREEN+'\t'+msg+'\t')
	network_layer(msg)
	return

def network_layer(msg):
	print(Fore.RED+'\n\n\n------------------NETWORK LAYER----------------------\n\n\n')
	ip=input(Fore.WHITE+"\nEnter the Ip address : \n");
	net_header = '\n(NETWORK - ' +bin(int(ipaddress.IPv4Address(ip)))+ ") -"
	msg = net_header + msg
	print(Fore.GREEN+' '+msg+'\n')
	datalink_layer(msg)
	return

def datalink_layer(msg):
	# converting everything into bits
	print(Fore.RED+'\n\n\n------------------DATA-LINK LAYER----------------------\n\n\n')
	msg_in_bits = ""
	for c in msg:
		# convert each letter to ascii
		ascii_number = ord(c)
		# convert each ascii to an 8-bit word
		eight_bits = '{:08b}'.format(ascii_number)
		msg_in_bits += eight_bits
	msg = msg_in_bits
	# use bit setting
	# placing a 0 after 5 consecutive 1s is a simple find and replace
	msg.replace('11111', ' 111110 ')
	# add header
	msg = '\n(Header  - '+get_random_header() +')\n\nMESSGAGE - '+ msg
	print(Fore.GREEN+' '+msg+'\t')
	physical_layer(msg)
	return

def physical_layer(msg):
	print("\n\n")
	print(Fore.RED+'\n\n\n-----------------PHYSICAL LAYER----------------------\n\n\n')
	print(Fore.GREEN+"\nFinal result :\n", msg)
	print(Fore.BLUE+"\nsize : ", len(msg))
	print("\n\n")
	return

def main(message):
	application_layer(message)
	return

def get_random_header():
	header = ""
	# generate a random 32-bit header
	for i in range(0, 32):
		header += str(random.choice([0,1]))
	return header;

	print("\n\n")
message = input(Fore.WHITE+"Enter A Message to UnderStand the All OSI Model Phases  ...\n")
main(message)