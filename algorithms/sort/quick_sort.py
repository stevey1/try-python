def sort(a, start, end):
    if(start < end):
        pivot = partition(a, start, end)
        sort(a, start, pivot-1)
        sort(a, pivot+1, end)


def partition(a, start, end):
    j = start - 1
    separator = a[end]
    for i in range(start, end):
        if a[i] < separator:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[end], a[j+1] = a[j+1], a[end]
    return j+1


print('adasdf22', __name__)
if __name__ == "__main__":
    b = ['d', 'e', 'a', 'c', 'b']
    sort(b, 0, len(b)-1)
