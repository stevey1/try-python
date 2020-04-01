# Search a sorted array by repeatedly dividing the search interval in half
def binarySearch(a,start, end, x):
    if end< start:
        return -1
    m=(end-start)//2
    if a[m]==x:
        return m
    if a[m]<x:
        return binarySearch(a, m, end,x)
    return binarySearch(a, start, m,x)
    
if __name__ == "__main__":
    a = [10, 20, 80, 30, 60, 50, 130, 100, 110, 170]
    a.sort()
    assert(binarySearch( a,0,len(a)-1, 30)==2)
