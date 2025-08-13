# mpiexec -n 5 python mpi_all2all.py
import numpy as np 
from mpi4py import MPI 

comm = MPI.COMM_WORLD
size = comm.Get_size() # total #processes
rank = comm.Get_rank() 

senddata = (rank+1)*np.arange(size, dtype=int)
recvdata = np.empty(size, dtype=int)

comm.Alltoall(senddata, recvdata)

print(f" process {rank} sending {senddata} receiving {recvdata}")
