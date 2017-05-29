
Visual Tracert
by Rashel Strigevsky
=========================
A final project for Gvahim program. The project is used in order to view a rout of a packet on the Internet.
The original traceroute program was written by Van Jacobson in 1987.
The project produces the user 2 services:
 - Textual Tracert
       The user gets textual output in the cmd - 
       serial number , ip address (hop)

 - Visual Tracert
       The user enters an ip address or a name of site (dns) and sees the route on a beautiful map.

EXECUTION
---------
Textual Tracert:

> cd [location of TextTracert.py file]
$ TextTracert.py --address [args]

Visual Tracert:

> cd [location of http_server.py file]
$ http_server.py

Open a web server and use the line:
http://localhost:8080/UserAgent.html
