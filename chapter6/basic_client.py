import socket 

# client socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get server host:port
host = socket.gethostname() 
port = 9999
# setup connection 
s.connect((host, port))
# receive no more than 1024 bytes
tm = s.recv(1024)
s.close()
print(f"Time connection server: {tm.decode('ascii')}")