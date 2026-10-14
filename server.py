
from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)

print("HealOps website running on port 8000")

server.serve_forever()
