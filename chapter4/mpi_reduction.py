# mpiexec -n 10 python mpi_reduction.py
import numpy
from mpi4py import MPI 

comm = MPI.COMM_WORLD 
size = comm.size # number of processes 
rank = comm.rank # current process id

array_size = 10
# process0 sends [0,1,2...,9]; process1 sends [0,2,...,18];
# = process0 sends "0" to process0, sends "1" to process1, ...; process1 sends 0 to process0, sends 2 to process1
senddata = (rank+1)*numpy.arange(array_size, dtype=int) 
recvdata = numpy.zeros(array_size, dtype=int) # [0,0,...,0] 

print(f" process {rank} sending {senddata}")
# process0 receives [0,...,0] from all processes; process1 receives [1,2,4...] from all; ...
# all is "reduce"="addup" => process0 added-up to 0; process1 added-up to 55; ...
# then that [0,55,...] added-up of 10 processes is stored in root (i.e. rank=0)
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)
print(f"on task {rank} after Reduce: data={recvdata}")
