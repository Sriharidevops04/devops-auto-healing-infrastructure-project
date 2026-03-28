# app2.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Response from Server 2")

server = HTTPServer(("0.0.0.0", 8002), handler)
server.serve_forever()
