# in-place sorting
# Internal and External Sortings?


def sort(a):
    l = len(a)
    m = l // 2
    a1 = a[:m]
    a2 = a[m:]
    if (m > 1):
        sort(a1)
    if (m+1 < l):
        sort(a2)

    i = 0
    i1 = 0
    i2 = 0
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] > a2[i2]:
            a[i] = a2[i2]
            i2 += 1
        else:
            a[i] = a1[i1]
            i1 += 1
        i = i+1
    if i2 < len(a2):
        a[len(a1)+i2:] = a2[i2:]
    if i1 < len(a1):
        a[len(a2)+i1:] = a1[i1:]
