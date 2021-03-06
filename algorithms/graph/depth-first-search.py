from collections import defaultdict 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v): 
  
        # Mark the current node as visited and print it 
        if self.visited[v]:
            return 

        self.visited[v]= True
        print (v)
  
        # Recur for all the vertices adjacent to 
        # this vertex 
        for i in self.graph[v]: 
            self.DFSUtil(i) 
  
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self): 
        self.visited =[False]*len(self.graph)
  
        # Call the recursive helper function to print 
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(len(self.graph)): 
            self.DFSUtil(i)
if __name__=="__main__":
    g = Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    
    print ("Following is Depth First Traversal")
    g.DFS()