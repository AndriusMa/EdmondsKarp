import decimal
import time

def InitializeNeighbors(W):
  neighbors = {} # vertex neighbors list
  for vertex in range(len(W)): # initialize empty vertex edges array
    neighbors[vertex] = []
  for vertex, edges in enumerate(W): # for each vertex in the graph
    for neighbor, edge in enumerate(edges): # for each edge from vertex
      if edge > 0: # if vertex is equal to 0, it does not exist
        neighbors[vertex].append(neighbor)
        neighbors[neighbor].append(vertex)
  return neighbors

def EdmondsKarp(W, neighbors, source, sink):
  flow = 0
  n = len(W)
  flows = [[0 for i in range(n)] for j in range(n)]
  while True:
    maximum_flow, parent = Bfs(W, neighbors, flows, source, sink)
    if maximum_flow == 0:
      break
    flow = flow + maximum_flow
    v = sink
    while v != source: # retrace the route back to the source
      u = parent[v]
      flows[u][v] = flows[u][v] + maximum_flow
      flows[v][u] = flows[v][u] - maximum_flow
      v = u
  return flow

def Bfs(W, neighbors, flows, source, sink):
  n = len(W)
  parents = [-1 for i in range(n)]
  parents[source] = -2
  C = [0 for i in range(n)]
  C[source] = decimal.Decimal('Infinity') # since edge to source cannot be valued, any number is less than infinity

  queue = []
  queue.append(source)
  while queue:
    u = queue.pop(0)
    for v in neighbors[u]:
      if W[u][v] - flows[u][v] > 0 and parents[v] == -1: # in some cases when there is for example 0 - -1, need to double check if it's not source
        parents[v] = u
        C[v] = min(C[u], W[u][v] - flows[u][v])
        if v != sink:
          queue.append(v)
        else:
          return C[sink], parents
  return 0, parents

if __name__ == "__main__":
  type_of_run = input("Enter the input choice: \n1 - From file\n2 - Choose from existing graphs\n")
  if type_of_run == str(1):
    file_name = input("Enter the file name:")
    try:
      file_object = open(file_name, "r")
    except FileNotFoundError:
      print("File with provided name does not exist")
      exit(-1)
    W = []
    source = 0
    sink = -1
    for line in file_object.readlines():
      W.append([int(i) for i in line.split(',')])
      sink += 1
    print(sink)
  elif type_of_run == str(2):
    input_val = input("Enter the graph number (1-4): ")

    if input_val == str(1):
      # Graph 1
      # node A  B  C  D  E  F  G
      W = [[ 0, 3, 0, 3, 0, 0, 0 ],  # A
          [ 0, 0, 4, 0, 0, 0, 0 ],   # B
          [ 0, 0, 0, 0, 2, 0, 0 ],   # C
          [ 0, 0, 0, 0, 0, 6, 0 ],   # D
          [ 0, 0, 0, 0, 0, 0, 1 ],   # E
          [ 0, 0, 0, 0, 0, 0, 9 ],   # F
          [ 0, 0, 0, 0, 0, 0, 0]]    # G

      source = 0  # A
      sink = 6    # G

    elif input_val == str(2):
      # Graph 2
      # node A  B  C  D  E  F  G  H  I  J  K  L  M  N
      W = [[ 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],  # A
          [ 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],   # B
          [ 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],   # C
          [ 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0 ],   # D
          [ 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0 ],   # E
          [ 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0 ],   # F
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0 ],   # G
          [ 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0 ],   # H
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0 ],   # I
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0 ],   # J
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0 ],   # K
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0 ],   # L
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6 ],   # M
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]   # N

      source = 0  # A
      sink = 13   # N

    elif input_val == str(3):
      # Graph 3
      # node A  B  C  D  E  F  G
      W = [[ 0, 3, 3, 3, 0, 0, 0 ],  # A
          [ 0, 0, 4, 0, 0, 0, 0 ],   # B
          [ 0, 0, 0, 1, 2, 2, 0 ],   # C
          [ 0, 0, 0, 0, 0, 6, 3 ],   # D
          [ 0, 1, 0, 2, 0, 2, 1 ],   # E
          [ 0, 0, 0, 0, 0, 0, 9 ],   # F
          [ 0, 0, 0, 0, 0, 0, 0]]    # G

      source = 0  # A
      sink = 6    # G

    elif input_val == str(4):
      # Graph 4
      # node A  B  C  D  E 
      W = [[ 0, 3, 3, 3, 0 ],   # A
          [ 0, 0, 4, 0, 9 ],    # B
          [ 0, 0, 0, 1, 0 ],    # C
          [ 0, 0, 0, 0, 6 ],    # D
          [ 0, 0, 0, 0, 0 ]]    # E

      source = 0   # A
      sink = 4     # E

    else:
      print("Invalid input")
      exit(-1)
  else:
    print("Invalid input")
    exit(-1)

  counter = 0
  time_before = time.time()
  #while counter <= 500000: # for running time check
  neighbors = InitializeNeighbors(W)
  max_flow = EdmondsKarp(W, neighbors, source, sink)
  #counter += 1
  #print("Time elapsed: " + str(time.time() - time_before))
  print("Max flow: " + str(max_flow))

  input("Press any key to exit")
