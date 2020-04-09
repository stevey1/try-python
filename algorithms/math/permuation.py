def Permutation (arr,m):
    n=len(arr)
    indices=[j+1 for j in range(m)]
    i=m-1
    while True:
        while indices[i]>n:
            indices[i]=i+1
            i-=1
            if i< 0: return
            indices[i]+=1
            arr[i:]=arr[i+1:]+arr[i:i+1]
        else:
            i=m-1
        print(arr[0:m])
        arr[i:]=arr[i+1:]+arr[i:i+1]
        indices[i]+=1

if __name__ == "__main__":
    arr=['a','b','c','d','e','f','g']
    Permutation (arr, 3)
    