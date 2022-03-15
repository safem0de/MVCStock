import urllib.request
import socket

class Connection:
        
    message = "y"

    def requestGoogle():
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False

    def connect(req=requestGoogle()):
        IPaddress=socket.gethostbyname(socket.gethostname())
        if req == False:
            Connection.message = "No internet, your localhost is "+ IPaddress
        else:
            Connection.message = "Connected, with the IP address: "+ IPaddress
        return Connection.message

# c = Connections()
# c.connect()
# print(c.message)