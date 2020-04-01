def heapify(arr, node): 
    n=len(arr)
    node1= node*2+1
    node2=node*2+2

    if (node1)<n:
        heapify(arr, node1) 
    if (node2)<n:
        heapify(arr, node2)
     
    if node1<n and arr[node]>arr[node1]:
        arr[node],arr[node1]=arr[node1],arr[node]
        heapify(arr, node1)
    if (node2)<n and arr[node]>arr[node2]:
        arr[node],arr[node2]=arr[node2],arr[node]
        heapify(arr, node2)


    if node1<n and node2<n and arr[node1]>arr[node2]:
        arr[node1],arr[node2]=arr[node2],arr[node1]
        heapify(arr, node2)

# The main function to sort an array of given size 
def heapSort(arr): 
    # Build a maxheap. 
    for i in range(0,len(arr),2):
        arr2=arr[i:]
        heapify(arr2, 0)
        arr[i:]=arr2

  
# Driver code to test above 
if __name__ == "__main__":
    arr = [ 12, 11, 13, 5, 6, 7,25,100,99,1,20,78,88,2,3,54,45,50,40] 
    heapSort(arr) 
    n = len(arr) 

    # This code is contributed by Mohit Kumra 