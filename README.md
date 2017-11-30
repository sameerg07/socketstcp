# socketstcp


						BUS BOOKING SYSTEM
AIM: To use sockets and establish a client-server connection using TCP connections between them.

Mainly our project aims to use sockets and do a back end for a bus booking system.We have used the basic socket package provided in python 2.7 along with threads and psycopg2 which is the python client for POSTGRESQL .

Our approach was to create threads for each process (i.e., client) and there by define a class with a default run function which runs on every ececution of the server file.

We have created a database named bus_ware in postgresql which has three tables bus_info which has the list of all the buses, route_table which has the routes for each bus between destinations and at last a seats table which has the seats information for a given bus on  a requested date.

In the client side we take the required information and receive it on the client side and thereby perform queries in the postgres database and fetch the results using the fetchall function and send the fetched information to the client.After each query we commit the changes on the database.

Features or the execution order of a transaction:
-> We invite the client and ask for the service either reservation or cancellation
-> if reservation , we ask for the date of journey 
-> then we ask for bus type either SLEEPER/SEMI_SLEEPER/SEATER
-> Then followed by the ac provsion AC/NON_AC
-> now , mainly the source and the destination
-> we send all the above information to the server and then display list the buses available between the desired stations.
-> the user selects the bus ID for the journey 
-> followed by the display of seats ,he selects the required seat
-> Fare is Displayed follwed by the confirmation of the ticket.
-> We have taken care of the intermediate vacancy of the seats i.e., a passenger can board a bus and take a seat which is vacant after a     	passenger gets down at a previous stop. For this we have used files and managed to save the information of all the passesngers along with 	their phone number , seat info , drop point. 
-> We have just taken the phone number for present to keep track of the passenger and his booked seat on  a particular date.
-> We then provided the option of cancelling the ticket which uodates the database in the back-end
-> In our policy we return back half of the fare to the passenger after cancellation.

SETUP:
1) Install postgresql in your linux system or windows
2) Install its python client psycopg2 (pip install psycopg2)
3) in the server.py, ihave connected postgres with my password, so just do a alter user and set your own password and then run it.
4)insert the tables given in datedb.sql else you can create one of your own but make sure to change the server.py accordingly.
5)run server.py and client.py parallely in two terminals and see the results.









Further improvements:
-> Mainly create a GUI
-> Authenticate each user , else there will be security issues.


TEAM MEMBERS:
GADICHERLA SAMEER 01FB15ECS101
ROHTIH GADAMSETTY 01FB15ECS100
GAGAN C J         01FB15ECS102

ignore the team information
