class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.distances=[[0 for i in range(len(matrix))] for j in range(len(matrix))]
        self.visited=[]
    def calculate_distance(self, begin):
        self.visited.append(begin)
        for vertex in self.matrix[begin]:
                self.distances[begin][vertex[0]] +=vertex[1] 
                self.distances[vertex[0]][begin]=self.distances[begin][vertex[0]]

        for vertex in self.matrix[begin]:
            if vertex[0] not in self.visited:
                self.calculate_distance(vertex[0])

if __name__ == "__main__":
    n = 6
  
    graph = [[] for i in range(n)] 
  
    # create undirected graph  
    # first edge  
    graph[0].append((1, 3))  
    graph[1].append((0, 3))  
  
    # second edge  
    graph[1].append((2, 4))  
    graph[2].append((1, 4))  
  
    # third edge  
    graph[1].append((5, 2))  
    graph[5].append((1, 2))  
  
    # fourth edge  
    graph[3].append((5, 6))  
    graph[5].append((3, 6))  
  
    # fifth edge  
    graph[4].append((5, 5))  
    graph[5].append((4, 5))  
    m = Matrix(graph)
    m.calculate_distance(0)
    print("Maximum length of cable =",m.distances) 