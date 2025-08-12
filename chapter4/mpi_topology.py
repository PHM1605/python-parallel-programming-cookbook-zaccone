# mpiexec -n 4 python mpi_topology.py
from mpi4py import MPI 
import numpy as np 

UP = 0 
DOWN = 1 
LEFT = 2
RIGHT = 3 

# if neighbour_processes = -1 => no proximity
neighbor_processes = [0,0,0,0]

if __name__ == "__main__":
  comm = MPI.COMM_WORLD 
  rank = comm.rank # current process id 
  size = comm.size # #processes total
  # calculate topology
  grid_rows = int(np.floor(np.sqrt(comm.size)))
  grid_column = comm.size // grid_rows 
  # safety
  if grid_rows*grid_column > size:
    grid_column -= 1
  if grid_rows * grid_column > size:
    grid_rows -= 1 
  # rank = 0 => building topology
  if (rank == 0):
    print(f"Building a {grid_rows}x{grid_column} grid topology:")
  cartesian_communicator = comm.Create_cart(
    (grid_rows, grid_column),  
    periods=(True, True), # no vertical wrap-around (e.g. moving down can return NULL); no horizontal wrap-around
    reorder=True) # MPI auto-reorder or not 
  # find location of the current process
  my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)
  # find neighbour
  neighbor_processes[UP], neighbor_processes[DOWN] = cartesian_communicator.Shift(0, 1)
  neighbor_processes[LEFT], neighbor_processes[RIGHT] = cartesian_communicator.Shift(1,1)
  print(f"Process#{rank} row={my_mpi_row} column={my_mpi_col}\n \
    --> up=process#{neighbor_processes[UP]}; down=process#{neighbor_processes[DOWN]}; \
    left=process#{neighbor_processes[LEFT]}; right=process#{neighbor_processes[RIGHT]}")
