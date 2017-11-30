# Python TCP Client A
import socket 

host = socket.gethostname() 
port = 2206
BUFFER_SIZE = 2000 
print "\n"
print "........Welcome to the Bus Resrvation......"
print "\n"

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
MESSAGE = raw_input("1. Reservation \n 2. Cancellation \n")
tcpClientA.send(MESSAGE) 

if MESSAGE == '1':
	MESSAGE = raw_input("Enter the date:(dd-mm)")
	tcpClientA.send(MESSAGE) 

	MESSAGE = raw_input("Enter the phone-no:")
	tcpClientA.send(MESSAGE) 


	MESSAGE = raw_input("Select the Type of the Bus :\n 1. SLEEPER \n 2. SEMI-SLEEPER \n 3. SEATER \n")
	tcpClientA.send(MESSAGE) 

	MESSAGE = raw_input("Select the AC PROVISION :\n 1. AC \n 2. NON-AC \n")
	tcpClientA.send(MESSAGE) 


	MESSAGE = raw_input("Enter the source:\n")
	MESSAGE = MESSAGE + ' '+raw_input("Enter the destination:\n")
	print MESSAGE
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print data,"\n"     #printing the buses between destinations

	data=tcpClientA.recv(2048)
	print "The fare for this Trip is:",data,"\n"     #printing the buses between destinations


	MESSAGE = raw_input("Enter the BUS NO:\n")
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print data,"\n"     #printing the seats between destinations

	MESSAGE = raw_input("Enter the SEAT NO:\n")
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print data,"\n"#updated printing the seats between destinations

	MESSAGE = raw_input("EVERYTHING DONE?:\n")
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print data,"\n"

elif MESSAGE == '2':
	MESSAGE = raw_input("Enter the date:(dd-mm)")
	tcpClientA.send(MESSAGE) 



	MESSAGE = raw_input("Select the Type of the Bus :\n 1. SLEEPER \n 2. SEMI-SLEEPER \n 3. SEATER \n")
	tcpClientA.send(MESSAGE) 

	MESSAGE = raw_input("Select the AC PROVISION :\n 1. AC \n 2. NON-AC \n")
	tcpClientA.send(MESSAGE) 


	MESSAGE = raw_input("Enter the source:\n")
	MESSAGE = MESSAGE + ' '+raw_input("Enter the destination:\n")
	print MESSAGE
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print data,"\n"     #printing the buses between destinations

	MESSAGE = raw_input("Enter the BUS NO:\n")
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print data,"\n"     #printing the seats between destinations

	MESSAGE = raw_input("Enter the SEAT NO:\n")
	tcpClientA.send(MESSAGE)

	data=tcpClientA.recv(2048)
	print "The return fare for this Trip is:",data,"\n"




	#data=tcpClientA.recv(2048)
	#print data,"\n"




'''
while MESSAGE != '0':
	print("Entered\n")
	tcpClientA.send(MESSAGE)     #echo
	data= tcpClientA.recv(BUFFER_SIZE)
	print (data)
	MESSAGE = raw_input("1. Show list \n 2. Exit \n Enter your choice: ") 
'''
tcpClientA.close()


