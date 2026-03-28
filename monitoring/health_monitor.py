import requests
import os

servers = {
    "http://localhost:8001": "app1",
    "http://localhost:8002": "app2"
}

for server in servers:
    try:
        requests.get(server, timeout=2)
        print(f"{server} is UP")
    except:
        print(f"{server} is DOWN → Restarting...")
        os.system("../automation/restart_server.sh")
