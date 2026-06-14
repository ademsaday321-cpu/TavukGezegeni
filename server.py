import os, http.server, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 4000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Sunucu http://localhost:{PORT} adresinde calisiyor...")
    httpd.serve_forever()
