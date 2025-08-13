# client asks server for a file "mytext.txt" on server
# server sends it back to client, saving as "received.txt"
import socket 

client_socket = socket.socket()
# host:port of server
host = socket.gethostname()
port = 60000
client_socket.connect((host, port))
client_socket.send("HelloServer!".encode())

with open("received.txt", "wb") as f:
  print("file opened")
  while True:
    print("receiving data...")
    data = client_socket.recv(1024)
    if not data:
      break
    print("Data => ", data.decode())
    f.write(data)
  f.close()
  print("Successfullly get the file")
  client_socket.close()
  print("connection closed")