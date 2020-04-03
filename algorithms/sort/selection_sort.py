def sort(a):
    n = len(a)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        if i != minIndex:
            a[i], a[minIndex] = a[minIndex], a[i]
    return a
