from http.server import BaseHTTPRequestHandler, HTTPServer
from tendo import singleton
import time
import pyperclip as pc
import urllib.parse
me = singleton.SingleInstance() # will sys.exit(-1) if other instance is running

# lookup your hostName using `ipconfig` on Windows
hostName = "192.168.0.16"
serverPort = 4646

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        decodedPath = urllib.parse.unquote(self.path[1:])
        (path, content) = decodedPath.split("/", 1)
        if path == "clipboard":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            pc.copy(content)
            print("copied to clipboard:")
            print(pc.paste())
        else:
            self.send_response(500)
            print("unknown requese:")
            print(self.path)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")