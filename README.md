# socketstcp
<h1 align="center">BUS BOOKING SYSTEM</h1>
<h3>AIM: To use sockets and establish a client-server connection using TCP connections between them.</h3>
<p>Mainly our project aims to use sockets and do a back end for a bus booking system.We have used the basic socket package provided in python 2.7 along with threads and psycopg2 which is the python client for PostgreSQL.<br>Our approach was to create threads for each process (i.e., client) and thereby define a class with a default run function which runs on every execution of the server file.<br>We have created a database named bus_ware in PostgreSQL which has three tables bus_info which has the list of all the buses, route_table which has the routes for each bus between destinations and at last a seats table which has the seats information for a given bus on a requested date.<br>In the client side we take the required information and receive it on the client side and thereby perform queries in the postgres database and fetch the results using the fetch_all function and send the fetched information to the client.<br>After each query we commit the changes on the database.</p>
<p>
	<ul><h4>Features or the execution order of a transaction:</h4>
	<li>We ask the client for the service either reservation or cancellation</li>
	<li>If reservation, we ask for the date of journey</li>
	<li>Then we ask for bus type either <b>SLEEPER/SEMI_SLEEPER/SEATER</b></li>
	<li>Then followed by the <em>ac_provision</em> <b>AC/NON_AC</b></li>
	<li>now, mainly the source and the destination</li>
	<li>We send all the above information to the server and then display list the buses available between the desired stations.</li>
	<li>The user selects the bus ID for the journey</li>
	<li>Followed by the display of seats, he selects the required seat</li>
	<li>Fare is Displayed followed by the confirmation of the ticket.</li>
	<li>We have taken care of the intermediate vacancy of the seats i.e., a passenger can board a bus and take a seat which is vacant after a passenger gets down at a previous stop.<br>For this we have used files and managed to save the information of all the passengers along with their phone number, seat info, drop point.</li>
	<li>We have just taken the phone number for present to keep track of the passenger and his booked seat on a particular date.</li>
	<li>We then provided the option of cancelling the ticket which updates the database in the back-end</li>
	<li>In our policy we return back half of the fare to the passenger after cancellation.</li>
	</ul>
</p>


<p><h4>SETUP:</h4><ol>
	<li>Install postgresql in your linux system or windows</li>
	<li>Install its python client psycopg2 (pip install psycopg2)</li>
<li>In the server.py, we have connected postgres with my password, so just do a alter user and set your own password and then run it.</li>
<li>Insert the tables given in datedb.sql else you can create one of your own but make sure to change the server.py accordingly.</li>
	<li>Run server.py and client.py parallely in two terminals and see the results.</li>
</ol></p>
<ul>Further improvements:
	<li>Mainly create a GUI</li>
	<li>Authenticate each user, else there will be security issues.</li>
</ul>
<ul>TEAM MEMBERS:
	<li><a href="https://www.linkedin.com/in/sameerg07/">Gadicherla Sameer</a></li>
	<li><a href="http://www.google.com/profiles/107164665008178006276">Rohith Gadamshetty</a></li>
	<li><a href="https://www.linkedin.com/in/gaganjchandra-29011998/">Gagan C J</a></li>
</ul>

> Ignore the team information
