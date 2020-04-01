# Python3 program for Fibonacci search.
# Returns index of x if present, else
# returns -1
# Don't understand



def fibMonaccianSearch(arr, x):
    #Get 2 fib numbers
    fibMn2,fibMn1 = 0,1 
    while (fibMn2 + fibMn1 < len(arr)):
        fibMn2,fibMn1 = fibMn1,fibMn2 + fibMn1

    offset = 0
    while (fibMn1 > 0):
        #User fib 2 to split and check
        if (arr[offset+fibMn2]== x):
            return offset+fibMn2
        #If not found, use next fib number to check
        if (arr[offset+fibMn2] < x):
            offset += fibMn2
        fibMn2,fibMn1 = fibMn1-fibMn2,fibMn2

    return -1

# Driver Code
arr = [10, 22, 35, 40, 45, 50,
       80, 82, 85, 90, 100, 110, 111]

x = 111
print("Found at index:",
      fibMonaccianSearch(arr, x))
