import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
import csv
import psycopg2
#fp = open('final.txt', 'a')

##print final
# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
	def __init__(self,ip,port): 
		Thread.__init__(self) 
		self.ip = ip 
		self.port = port 
		#print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
	def run(self):
		#while True: 
		data = conn.recv(2048)
		MESSAGE = " "
		service = data 
		print "Option Chose:\n",data
	    #MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
		if(data=='1'):
			conn_data = psycopg2.connect(database = "bus_ware", user = "postgres", password="sameer", host = "localhost", port = "5432")
			cur = conn_data.cursor()
			
			data = conn.recv(2048)
			if(data == '24-11'):
				date_chosen = '1'
			if(data == '25-11'):
				date_chosen = '2'

			data = conn.recv(2048)
			phone_no = data
			
			data = conn.recv(2048)
			if(data == '1'):
				type_chosen = 'SLEEPER'
			if(data == '2'):
				type_chosen = 'SEMI-SLEEPER'
			if(data == '3'):
				type_chosen = 'SEATER'
			
			data = conn.recv(2048)
			if(data == '1'):
				ac_chosen = '1'
			if(data == '2'):
				ac_chosen = '0'

			data = conn.recv(2048)
			source,destination = data.split(' ')
			print source,destination


			cur.execute("SELECT t2.bus_id , t1.name , t2.from_add , t2.to_add , t2.depart , t2.arrive , t2.fare from route_table t2 , bus_info t1 where t2.from_add ='"+source+"'and t2.to_add ='"+destination+"' and t1.bus_id=t2.bus_id and t1.a_c_fact='"+ac_chosen+"'and t1.bus_type='"+type_chosen+"'")
			conn_data.commit()
			rows = cur.fetchall()
			MESSAGE = "BUS NO\t \t NAME \t \t FROM_PLACE \t\t TO_PLACE \t depart \t arrive \t fare \n"
			for row in rows:
				#print type(row[0])
				#print type(row[1])
				#print type(row[2])
				#print type(row[3])
				#print type(row[4])
				#print type(row[5])
				#print type(row[6])
				MESSAGE = MESSAGE + row[0] + "\t\t\t" + row[1] + "\t\t\t" + row[2] + "\t\t\t" + row[3] +  "\t\t\t" + str(row[4]) + "\t\t\t" + str(row[5])+ str(row[6]) + "\n"
				
			
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
			conn.send(MESSAGE)


			cur.execute("SELECT t2.fare from route_table t2 , bus_info t1 where t2.from_add ='"+source+"'and t2.to_add ='"+destination+"' and t1.bus_id=t2.bus_id and t1.a_c_fact='"+ac_chosen+"'and t1.bus_type='"+type_chosen+"'")
			rows = cur.fetchall()
			for row in rows:
				fare = row[0]
			FARE = str(fare)
			conn.send(FARE)	



			data = conn.recv(2048)
			chosen_id = str(data)
			cur.execute("SELECT bus_id , no_seats , seat_type , status from seats where bus_id ='"+chosen_id+"' and date_int='"+date_chosen+"'")
			conn_data.commit()
			rows = cur.fetchall()
			MESSAGE = "BUS NO\tSEAT NO\tTYPE \tSTATUS \n"
			for row in rows:
				MESSAGE = MESSAGE + row[0] + " \t " + str(row[1]) + "\t " + row[2] + "\t" + row[3] + "\n"
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
			conn.send(MESSAGE)

			data = conn.recv(2048)
			chosen_seat = data
			cur.execute("SELECT status from seats where no_seats ='"+chosen_seat+"' and date_int='"+date_chosen+"'")
			rows = cur.fetchall()
			for row in rows:
				check_status = row[0]
			print check_status,'\n'
			if(check_status == 'OCCUPIED'):
				#print final
				for i in final:
					'''if chosen_id == i[0]:
						print "true for id"
					if int(chosen_seat) == i[1][0]:
						print "type true for seat"
					print source
					if source == i[1][1]:
						print "true for destination"
					print 1
					'''
					if chosen_id == i[0] and int(chosen_seat) == i[1][0] and source == i[1][1] and date_chosen == i[2]:
						#print 2
						cur.execute("UPDATE seats SET status = 'OCCUPIED' where no_seats ='"+chosen_seat+"'and date_int='"+date_chosen+"'and bus_id='"+chosen_id+"'")
						#print 3
						#conn_data.commit()
						#print 1
						cur.execute("SELECT bus_id , no_seats , seat_type , status from seats where bus_id ='"+chosen_id+"'and date_int='"+date_chosen+"'")
						#print 4
						#conn_data.commit()
						rows = cur.fetchall()
						#print 5
						MESSAGE = "BUS NO\t \t SEAT NO \t \t TYPE \t\t STATUS \n"
						for row in rows:
							MESSAGE = MESSAGE + row[0] + "\t" + str(row[1]) + "\t" + row[2] + "\t" + row[3] + "\n"
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
						#final.remove(i)
						#print 6
						fp.write('\n'+str(chosen_id)+' '+str(chosen_seat)+' '+str(destination)+' '+str(phone_no)+' '+str(date_chosen))
						#print 7
						#final.append([chosen_id,[chosen_seat,destination]])
						#print final
						conn_data.commit()
						break
					MESSAGE = MESSAGE + "sorry it's already booked :( \n"
			elif check_status == 'UNOCCUPIED' :
				cur.execute("UPDATE seats SET status = 'OCCUPIED' where no_seats ='"+chosen_seat+"'and date_int='"+date_chosen+"'and bus_id='"+chosen_id+"'")
				conn_data.commit()
				cur.execute("SELECT bus_id , no_seats , seat_type , status from seats where bus_id ='"+chosen_id+"' and date_int='"+date_chosen+"'")
				rows = cur.fetchall()
				MESSAGE = "BUS NO\t \t SEAT NO \t \t TYPE \t\t STATUS \n"
				for row in rows:
					MESSAGE = MESSAGE + row[0] + "\t" + str(row[1]) + "\t" + row[2] + "\t" + row[3] + "\n"
				#fp.write(str([chosen_id,[chosen_seat,destination]]))
				fp.write('\n'+str(chosen_id)+' '+str(chosen_seat)+' '+str(destination)+' '+str(phone_no)+' '+str(date_chosen))
				#print final
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
				#final.append([chosen_id,[chosen_seat,destination]])
			else:
				MESSAGE = MESSAGE + "sorry it's already booked :( \n"
			conn.send(MESSAGE)

			data=conn.recv(2048)
			if (data == 'YES'):
				MESSAGE = "Ticket has been booked:\n Seat no :"+str(chosen_seat)+"\n BUS NO:"+str(chosen_id) + "\n With Phone Number:"+str(phone_no)
			conn.send(MESSAGE)

		if(data=='2'):
			conn_data = psycopg2.connect(database = "bus_ware", user = "postgres", password="sameer", host = "localhost", port = "5432")
			cur = conn_data.cursor()
			
			data = conn.recv(2048)
			if(data == '24-11'):
				date_chosen = '1'
			if(data == '25-11'):
				date_chosen = '2'

			data = conn.recv(2048)
			if(data == '1'):
				type_chosen = 'SLEEPER'
			if(data == '2'):
				type_chosen = 'SEMI-SLEEPER'
			if(data == '3'):
				type_chosen = 'SEATER'
			
			data = conn.recv(2048)
			if(data == '1'):
				ac_chosen = '1'
			if(data == '2'):
				ac_chosen = '0'

			data = conn.recv(2048)
			source,destination = data.split(' ')
			print source,destination


			cur.execute("SELECT t2.bus_id , t1.name , t2.from_add , t2.to_add , t2.depart , t2.arrive , t2.fare from route_table t2 , bus_info t1 where t2.from_add ='"+source+"'and t2.to_add ='"+destination+"' and t1.bus_id=t2.bus_id and t1.a_c_fact='"+ac_chosen+"'and t1.bus_type='"+type_chosen+"'")
			conn_data.commit()
			rows = cur.fetchall()
			MESSAGE = "BUS NO\tNAME\tFROM_PLACE\tTO_PLACE\tdepart\tarrive\tfare \n"
			for row in rows:
				#print type(row[0])
				#print type(row[1])
				#print type(row[2])
				#print type(row[3])
				#print type(row[4])
				#print type(row[5])
				#print type(row[6])
				MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] +  "\t" + str(row[4]) + "\t" + str(row[5])+ str(row[6]) + "\n"
				
			
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
			conn.send(MESSAGE)


			data = conn.recv(2048)
			chosen_id = str(data)
			cur.execute("SELECT bus_id , no_seats , seat_type , status from seats where bus_id ='"+chosen_id+"' and date_int='"+date_chosen+"'")
			conn_data.commit()
			rows = cur.fetchall()
			MESSAGE = "BUS NO\t \t SEAT NO \t \t TYPE \t\t STATUS \n"
			for row in rows:
				MESSAGE = MESSAGE + row[0] + "\t" + str(row[1]) + "\t" + row[2] + "\t" + row[3] + "\n"
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
			conn.send(MESSAGE)

			data = conn.recv(2048)
			chosen_seat = data
			cur.execute("SELECT status from seats where no_seats ='"+chosen_seat+"'and date_int='"+date_chosen+"'and bus_id='"+chosen_id+"'")
			conn_data.commit()
			rows = cur.fetchall()
			for row in rows:
				check_status = row[0]
			print check_status,'\n'
			if check_status == 'OCCUPIED':
				cur.execute("UPDATE seats SET status = 'UNOCCUPIED' where no_seats ='"+chosen_seat+"'and date_int='"+date_chosen+"'")
				conn_data.commit()
				cur.execute("SELECT bus_id , no_seats , seat_type , status from seats where bus_id ='"+chosen_id+"'and date_int='"+date_chosen+"'")
				rows = cur.fetchall()
				MESSAGE = "BUS NO\t \t SEAT NO \t \t TYPE \t\t STATUS \n"
				for row in rows:
					MESSAGE = MESSAGE + row[0] + "\t" + str(row[1]) + "\t" + row[2] + "\t" + row[3] + "\n"
				#MESSAGE = MESSAGE + row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + str(row[3]) +  "\t" + str(row[4]) + "\t" + str(row[5])+ "\n"
			else:
				MESSAGE = MESSAGE + "sorry it's already vacant :( \n"

			cur.execute("SELECT t2.fare from route_table t2 , bus_info t1 where t2.from_add ='"+source+"'and t2.to_add ='"+destination+"' and t1.bus_id=t2.bus_id and t1.a_c_fact='"+ac_chosen+"'and t1.bus_type='"+type_chosen+"'")
			rows = cur.fetchall()
			for row in rows:
				fare = row[0]
			fare = fare/2
			FARE = str(fare)+'\n'
			conn.send(FARE)

			conn.send(MESSAGE)




		else:

			MESSAGE = "User terminated"#select * from t1 where t1.id='a'
		data = '200'
		#for i in range(0,2):
		#conn.send(MESSAGE)  # echo 

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT =2206
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
	final = []
	fp = open('final.txt', 'a')
	with open('final.txt' , 'r') as f:
		res = f.readlines()
		print res
		for i in range(1,len(res)):
			res1 = res[i].strip().split(' ')
			final.append([res1[0],[int(res1[1]),res1[2]],res1[4]])
		print final
	tcpServer.listen(4) 
	print "Multithreaded Python server : Waiting for connections from TCP clients..." 
	(conn, (ip,port)) = tcpServer.accept() 
	newthread = ClientThread(ip,port) 
	newthread.start() 
	threads.append(newthread) 
	fp.close()
 
for t in threads: 
    t.join()
