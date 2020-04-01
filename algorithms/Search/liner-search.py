# Also called Squential Search
# Python 3 implementation of the approach

# Linearly search x in arr[]. If x is present
# then return the index, otherwise return -1
def search(arr, x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [1, 10, 30, 15]
    assert(search(arr, 30),3)
