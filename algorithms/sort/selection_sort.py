def sort(a):
    n = len(a)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]

if __name__ == "__main__":
    a = ['d', 'a', 'c', 'b']
    sort(a)
    assert( a==['a','b','c','d'])