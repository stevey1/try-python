from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def bf(self, startNode):
        c=list()
        d=[]
        assert(c==d)
        visited=[False] * len(self.graph)
        queue=[startNode]
        while(queue):
            vertex=queue.pop(0)
            print(vertex, end=" ")
            visited[vertex]=True
            for i in self.graph[vertex]:
                if not visited[i]:
                    queue.append(i)
if __name__=="__main__":
    g = Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    
    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)") 
    g.bf(2) 