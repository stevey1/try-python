# Search a sorted array by repeatedly dividing the search interval in half
def binarySearch(x, a):
    start = 0
    end = len(a)-1
    a.sort()
    while end >= start:
        m = (end + start)//2
        if a[m] == x:
            return m
        if a[m] > x:
            end = m-1
        else:
            start = m+1
    return -1


x = 130
a = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
print(binarySearch(x, a))
