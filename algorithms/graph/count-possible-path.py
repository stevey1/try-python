from collections import defaultdict 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    # Constructor 
    def __init__(self, vertices): 
  
        # default dictionary to store graph 
        self.graph = [[] for i in range(vertices)]
        self.trail=[]
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def countPaths (self, start, end): 
        self.trail.append(start)
        if start==end:
            return 1        
        if not self.graph[start]:
            return 0
        count=0
        for vertex in self.graph[start]:
            if vertex not in self.trail:
                count +=self.countPaths(vertex,end)
                self.trail.pop()

        return count
            
if __name__=="__main__":
    g = Graph(4)  
    g.addEdge(0, 1)  
    g.addEdge(0, 2)  
    g.addEdge(0, 3)  
    g.addEdge(2, 0)  
    g.addEdge(2, 1)  
    g.addEdge(1, 3)  
    print(g.countPaths(2, 3)) 