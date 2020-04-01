#Euler path:  only 1 or 2 vertex has odd number edges 
#Euler circuit: all vertex has even number edges
def findpath(graph): 
    n = len(graph) 
    numOfEdges=[]

    minEdges=1000000000000000000000000000000000000000000

    # Find out how many vertex has odd number edges 
    numOfOdd = 0
    for i in range(n):
        numOfEdges.append(sum(graph[i]))
        if numOfEdges[i] % 2 == 1: 
            numOfOdd += 1
            if numOfOdd > 2: 
                print("No Solution") 
                return
            if minEdges>numOfEdges[i]:
                cur = i 
                minEdges=numOfEdges[i]

  
    # If there is a path find the path 
    # Initialize empty stack and path 
    # take the starting current as discussed 
    path = [str(cur+1)]  
  
    # Loop will run until there is element in the stack 
    # or current edge has some neighbour. 
    while numOfEdges[cur] != 0: 
        # If the current vertex has at least one 
        # neighbour add the current vertex to stack, 
        # remove the edge between them and set the 
        # current to its neighbour. 
        print (graph)

        for i in range(n): 
            if graph[cur][i] == 1: 
                graph[cur][i] = 0
                graph[i][cur] = 0
                numOfEdges[cur]-=1
                numOfEdges[i]-=1
                cur = i 
                path.append(str(cur+1)) 
                break
    # print the path 
    #print (path)
    print (" -> ".join(path))

if __name__ == "__main__":
    graph1 = [[0, 1, 0, 0, 1], 
            [1, 0, 0,0, 0], 
            [0, 0, 0, 1, 1], 
            [0, 0, 1, 0, 1], 
            [1, 0, 1, 1, 0]] 
    findpath(graph1)