def sort(a):
    for k in range(len(a)):
        for i in range(len(a)-1-k):
            j = i+1
            if(a[i] > a[j]):
                a[i], a[j] = a[j], a[i]

