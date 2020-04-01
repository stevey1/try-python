def sort(a):
    for k in range(len(a)):
        for i in range(len(a)-1-k):
            if(a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
if __name__ == "__main__":
    a = ['d', 'a', 'c', 'b']
    sort(a)
    assert( a==['a','b','c','d'])