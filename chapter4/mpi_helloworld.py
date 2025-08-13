# mpiexec -n 5 python mpi_helloworld.py
from mpi4py import MPI 

comm = MPI.COMM_WORLD 
rank = comm.Get_rank()
print("hello world from process ", rank)
