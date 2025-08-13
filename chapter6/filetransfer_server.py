# client asks server for a file "mytext.txt" on server
# server sends it back to client, saving as "received.txt"

import socket


port = 60000
server_socket = socket.socket()
host = socket.gethostname()
server_socket.bind((host, port))
server_socket.listen(15) # listen to 15 client's requests
print("Server listening...")

while True:
  conn, addr = server_socket.accept() # "conn" is data socket
  print("Got connection from ", addr)
  data = conn.recv(1024)
  print("Server received", repr(data.decode())) # random "helloserver" message
  filename = "mytext.txt"
  f = open(filename, "rb")
  l = f.read(1024)
  while l:
    conn.sendall(l)
    print("Sent", repr(l.decode()))
    l = f.read(1024)
  # close file after done sending 
  f.close()
  print("Done sending")
  conn.close()

