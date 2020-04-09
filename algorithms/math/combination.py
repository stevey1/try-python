def combination(arr,m):
    n=len(arr)
    indices=[j for j in range(m)]

    i =m-1
    while True:
        while indices[i]==n+i-m+1:
            indices[i]=i
            i-=1
            if i<0: return
            indices[i]+=1
            #reset indices
            for j in range(i+1, m):
                indices[j]=indices[j-1]+1

            if indices[i]<n+i-m+1:
                i=m-1
                break
            #print
        for j in range(m):
            print (arr[indices[j]], end="")
        print("")
        indices[i]+=1

if __name__ == "__main__":
    arr=['a','b','c','d','e','f','g']
    combination(arr, 4)
    