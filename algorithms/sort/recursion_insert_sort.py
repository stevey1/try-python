def insertionSortRecursive(arr,n): 
    # base case 
    if n<=1: 
        return
    print("entering", n)  
    # Sort first n-1 elements 
    insertionSortRecursive(arr,n-1) 
    '''Insert last element at its correct position 
        in sorted array.'''
    j = n-1
    print("calculate", j)
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position  
    while (j>0 and arr[j-1]>a[j]): 
        print("test", j, arr[j])
        arr[j] ,arr[j-1] =arr[j-1] , arr[j] 
        j = j-1
  

if __name__ == "__main__":
    a = ['d', 'a', 'c', 'b']
    insertionSortRecursive(a,len(a))
    print(a)
    assert( a==['a','b','c','d'])