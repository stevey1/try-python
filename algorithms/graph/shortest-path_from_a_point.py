class Graph():
    def __init__(self,v):
        self.matrix=[[0 for i in range(v)] for j in range(v)]
        self.visited=[]
        self.diestances=[0]*v
    def addEdgeRev(self,u,v,distince):
        self.matrix[u][v]=distince

    def depth_first_shortest_path(self, curr, start):
        self.visited.append(curr)
        for vertex in range(len(self.matrix[curr])):
            if self.matrix[curr][vertex] >0 and not vertex==start:
                if self.diestances[vertex]>0:
                    self.diestances[vertex]= min(self.diestances[vertex], self.diestances[curr]+self.matrix[curr][vertex])
                else:
                    self.diestances[vertex]= self.diestances[curr]+self.matrix[curr][vertex]
                if vertex not in self.visited:                                                                                                                                                                                                                                                                                                                                                  
                    self.depth_first_shortest_path(vertex,start)
                    self.visited.pop()

    def breath_first_shortest_path(self, curr):
        self.visited.append(curr)
        for vertex in range(len(self.matrix[curr])):
            if vertex not in self.visited and self.matrix[curr][vertex]>0:
                if self.diestances[vertex]>0:
                    self.diestances[vertex]= min(self.diestances[vertex], self.diestances[curr]+self.matrix[curr][vertex])
                else:
                    self.diestances[vertex]= self.diestances[curr]+self.matrix[curr][vertex]
        for vertex in range(len(self.matrix[curr])):
            if vertex not in self.visited and self.matrix[curr][vertex]>0:
                self.breath_first_shortest_path(vertex)
                
if __name__=="__main__":
    V = 5 
    g=Graph (V) 
  
    g.addEdgeRev(0, 2, 1) 
    g.addEdgeRev(0, 4, 5) 
    g.addEdgeRev(1, 4, 1) 
    g.addEdgeRev(2, 0, 10) 
    g.addEdgeRev(2, 3, 5) 
    g.addEdgeRev(3, 1, 1) 
    g.addEdgeRev(4, 0, 5) 
    g.addEdgeRev(4, 2, 100) 
    g.addEdgeRev(4, 3, 5)  
    
    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)") 
    #g.depth_first_shortest_path(0,0) 
    g.breath_first_shortest_path(0) 
    print ("g.diestances",g.diestances)