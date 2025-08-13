# we have 2 <sender> processes and 2 <receiver> process
# mpiexec -n 9 python mpi_p2p.py
from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.rank 
print("my rank is : ", rank)

## 2 <sender> processes
if rank == 0:
  data = 10000000
  destination_process = 4
  comm.send(data, dest=destination_process) # send data to process#4
  print(f"sending data {data} to process#{destination_process}")

if rank == 1:
  data = "hello"
  destination_process = 8
  comm.send(data, dest=destination_process) # send a different data to process#8
  print(f"sending data {data} to process#{destination_process}")

## 2 <receiver> processes
if rank == 4:
  data = comm.recv(source=0)
  print(f"data received is = {data}")

if rank == 8:
  data1 = comm.recv(source=1)
  print(f"data received is = {data1}")