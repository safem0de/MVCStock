import urllib.request
import urllib.error
import socket
import sys

class Connection:
        
    message = "y"

    def requestGoogle():
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except urllib.error.URLError as e:
            print(e.reason)
            return False

    try:
        def connect(req=requestGoogle()):
            IPaddress=socket.gethostbyname(socket.gethostname())
            if req == False or "10.121":
                Connection.message = "No internet, your localhost is "+ IPaddress
                # sys.exit(Connection.message)
            else:
                Connection.message = "Connected, with the IP address: "+ IPaddress
            return Connection.message
    except:
        print("No Internet")