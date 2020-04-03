# Also called Squential Search
# Python 3 implementation of the approach

# Linearly search x in arr[]. If x is present
# then return the index, otherwise return -1


def search(arr, x):
    n = len(arr)
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
arr = [1, 10, 30, 15]
x = 30
print(x, "is present at index",
      search(arr, x))
