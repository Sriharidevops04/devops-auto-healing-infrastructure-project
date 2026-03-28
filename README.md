Project title:
Nginx Load Balancer with Python Backend Servers

overview:
This project demonstrates how to build a simple yet powerful load balancing system using Nginx and Python backend servers. It simulates real-world production architecture where incoming traffic is distributed across multiple servers.

Architecutre:

Client (Browser / curl)
        ↓
     Nginx (Port 80)
        ↓
-------------------------
|        |              |
Server1  Server2    (More...)
:8001     :8002

Technologies Used:
Python (Flask)
Nginx
Linux (Ubuntu)
Networking Concepts
