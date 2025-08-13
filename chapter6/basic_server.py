import time, socket

# create a server-socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
# server listen to max 5 requests
serversocket.listen(5)
while True:
  clientsocket, addr = serversocket.accept()
  print(f"Connected with [addr]:[port] {str(addr)}") # this port from client will be different to 9999
  currentTime = time.ctime(time.time()) + "\n"
  clientsocket.send(currentTime.encode('ascii'))
  clientsocket.close()