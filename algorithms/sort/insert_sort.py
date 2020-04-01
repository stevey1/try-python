def sort(a):
    n = len(a)
    for i in range(n-1):
        j=i+1
        while j>0 and a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
            j=j-1

if __name__ == "__main__":
    a = ['d', 'a', 'c', 'b']
    sort(a)
    assert( a==['a','b','c','d'])