# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    print("i=",i,"l=",l,"r=",r)
  
    # See if left child of root exists and is 
    # greater than root 
    print("i=",arr[i])

    if l < n and arr[i] < arr[l]: 
        print("l=",arr[l])
        largest = l 

  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        print("r=",arr[r])
        largest = r 
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 

def heapify2(arr, node): 
    n=len(arr)
    if (node*2+1)<n:
        heapify2(arr, node*2+1) 
    if (node*2+2)<n:
        heapify2(arr, node*2+2)
     
    if 2*node+1<n and arr[node]<arr[2*node+1]:
        arr[node],arr[2*node+1]=arr[2*node+1],arr[node]
    if (2*node+2)<n and arr[node]<arr[2*node+2]:
        arr[node],arr[2*node+2]=arr[2*node+2],arr[node]
    if 2*node+1<n and 2*node+2<n and arr[2*node+1]<arr[2*node+2]:
        arr[2*node+1],arr[2*node+2]=arr[2*node+2],arr[2*node+1]

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
    print (" array is",arr) 
  
    # Build a maxheap. 
    heapify2(arr, 0) 
    # for i in range(round(n/2-0.01) - 2, -1, -1): 
    #     heapify2(arr, n, i) 
    print ("Sorted array is",arr) 
  
    One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
if __name__ == "__main__":
    arr = [ 12, 11, 13, 5, 6, 7] 
    heapSort(arr) 
    n = len(arr) 
    print ("Sorted array i2222s",arr) 

    # This code is contributed by Mohit Kumra 