# mpiexec -n 10 python mpi_gather.py
from mpi4py import MPI 

comm = MPI.COMM_WORLD 
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank+1)**2
data = comm.gather(data, root=0) 

if rank==0:
  print(f"rank = {rank} ... receiving data from other processes")
  for i in range(1, size):
    value = data[i]
    print(f" process 0 is receiving {value} from process {i}")
