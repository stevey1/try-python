def sort(a):
    n = len(a)
    for i in range(n):
        smallest = a[i]
        smallestIndex = i
        for j in range(i+1, n):
            if(a[j] < smallest):
                smallest = a[j]
                smallestIndex = j
        if i != smallestIndex:
            a[i], a[smallestIndex] = a[smallestIndex], a[i]


if __name__ == "__main__":
    a = ['d', 'a', 'c', 'b']
    sort(a)
