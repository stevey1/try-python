def heapify(arr, node): 
    n=len(arr)
    if (node*2+1)<n:
        heapify(arr, node*2+1) 
    if (node*2+2)<n:
        heapify(arr, node*2+2)
     
    if 2*node+1<n and arr[node]>arr[2*node+1]:
        arr[node],arr[2*node+1]=arr[2*node+1],arr[node]
        heapify(arr, 2*node+1)
    if (2*node+2)<n and arr[node]>arr[2*node+2]:
        arr[node],arr[2*node+2]=arr[2*node+2],arr[node]
        heapify(arr, 2*node+2)


    if 2*node+1<n and 2*node+2<n and arr[2*node+1]>arr[2*node+2]:
        arr[2*node+1],arr[2*node+2]=arr[2*node+2],arr[2*node+1]
        heapify(arr, 2*node+2)

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
    # Build a maxheap. 
    for i in range(0,n,2):
        arrb=arr[i:]
        heapify(arrb, 0)
        arr[i:]=arrb
        print ("Sorted array",arr) 

  
# Driver code to test above 
if __name__ == "__main__":
    arr = [ 12, 11, 13, 5, 6, 7,25,100,99,1,20,78,88,2,3,54,45,50,40] 
    heapSort(arr) 
    n = len(arr) 

    # This code is contributed by Mohit Kumra 