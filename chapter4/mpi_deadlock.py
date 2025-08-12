# mpiexec -n 9 python mpi_deadlock.py
# don't get this, it seems working ok. seems like lib works smartly to "wait"
from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.rank 
print(f"my rank is {rank}")

if rank == 1:
  data_send = "a"
  destination_process = 5
  source_process = 5
  # # method: send() and recv() separately
  # data_received = comm.recv(source=source_process)
  # comm.send(data_send, dest=destination_process)
  # better method: sendrecv()
  data_received = comm.sendrecv(data_send, dest=destination_process, source=source_process)
  # print out
  print(f"sending data {data_send} to process#{destination_process}")
  print(f"data received is = {data_received}")

if rank == 5:
  data_send = "b"
  destination_process = 1
  source_process = 1
  # # method: send() and recv() separately
  # comm.send(data_send, dest=destination_process)
  # data_received = comm.recv(source=source_process)
  # better method: sendrecv()
  data_received = comm.sendrecv(data_send, dest=destination_process, source=source_process)
  print(f"sending data {data_send} to process#{destination_process}")
  print(f"data received is = {data_received}")