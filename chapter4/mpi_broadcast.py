# mpiexec -n 10 python mpi_broadcast.py

from mpi4py import MPI 

comm = MPI.COMM_WORLD 
rank = comm.Get_rank()

# master process 
if rank == 0:
  variable_to_share = 100 
else:
  variable_to_share = None 

variable_to_share = comm.bcast(variable_to_share, root=0)
print(f"process = {rank} variable shared = {variable_to_share}")
