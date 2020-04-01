from collections import defaultdict
class Graph():
    def __init__(self, nodes):
        self.graph=[[] for i in range(nodes)]
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sorting(self, vertex):
        self.visited[vertex]=True

        for i in sorted(self.graph[vertex]):
            if not self.visited[i]:
                self.topological_sorting(i)
        self.stack.append(vertex)


    def sort(self):
        self.stack=[]
        self.visited=[False] * 6
        print(self.visited)
        for i in range(6):
            if not self.visited[i]:
                self.topological_sorting(i)
        while self.stack:
            vertex =self.stack.pop()
            print(vertex," ")

if __name__=="__main__":
    g= Graph(6) 
    g.addEdge(5, 2)
    g.addEdge(5, 0) 
    g.addEdge(4, 0) 
    g.addEdge(4, 1) 
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.sort()

  