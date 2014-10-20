class PathPlan:
  def __init__(self,coordinates):
    self.shortest_path = []
    self.cost = 0
    self.graph = {}
    self.coordinates = coordinates



  def dijkstra(self,graph,source,destination,visited=[],distances={},predecessors={}):

    if source not in graph:
      raise TypeError('Sorry, couldnt find starting point')
    if destination not in graph:
      raise TypeError('Sorry, couldnt find destination')    
        # ending condition
    if source == destination:
          #end case for recursion
      path=[]
      pred=destination
      while pred != None:
        path.append(pred)
        pred=predecessors.get(pred,None)
      print('shortest path: '+str(path)+" cost="+str(distances[destination])) 
      self.shortest = path
      self.cost = distances[destination]
        

    else :     
            # IF this is the first time ran, intialize source with no cost
      if not visited: 
        distances[source]=0
           #Check the connectiosn of the source
      for neighbor in graph[source] :
                #Make sure the node we are visitng hasn't been visited
        if neighbor not in visited:
          new_distance = distances[source] + graph[source][neighbor]
          if new_distance < distances.get(neighbor,float('inf')): #If value does not exist in distances we have not visited and nthis statement must return true
            distances[neighbor] = new_distance # Distance from source to neighbor = distance
            predecessors[neighbor] = source #Mark we have connected neighbor to its src
            # mark as visited
      visited.append(source)
            # now that all neighbors have been visited: recurse                         
            #Recursion, leap of faith style, run function on each minimum.
      unvisited={}
      for k in graph:
        if k not in visited:
          unvisited[k] = distances.get(k,float('inf')) 
                 
      x=min(unvisited, key=unvisited.get) #get is the function to get value of key, use that to sort and find minimum unvisited
          
      self.dijkstra(graph,x,destination,visited,distances,predecessors)
          
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

if __name__ == "__main__":
    # graph must be a dictioanry of nodes with the key as node name and the value a dictionary with keys nodes connnected to and value as their weight. 
  graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
    #returns = dijkstra(graph,'c','b')
    #print returns[0]
    #print returns[1]
  path = PathPlan([0,0])
  path.graph = graph
  path.dijkstra(path.graph,'c','b')