class Sort():
    @staticmethod
    def bubble_sort(a):
        for k in range(len(a)):
            for i in range(len(a)-1-k):
                if(a[i] > a[i+1]):
                    a[i], a[i+1] = a[i+1], a[i]

    @staticmethod
    def insert_sort(a):
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

    @staticmethod
    def merge_sort(a):
        n = len(a)
        m = n // 2
        l = a[:m]
        r = a[m:]
        if m > 1:
            Sort.merge_sort(l)
        if n > m+1:
            Sort.merge_sort(r)
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                a[k] = r[j]
                j += 1
            else:
                a[k] = l[i]
                i = i+1
            k = k+1
        if j < len(r):
            a[len(l)+j:] = r[j:]
        if i < len(l):
            a[len(r)+i:] = l[i:]
