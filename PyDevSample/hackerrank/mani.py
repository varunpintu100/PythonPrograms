def funtion123(n,arr):
    arr=sorted(arr)
    count=0
    for i in range(n):
        j=i+1
        if(j<n):
            if(arr[i]+1==arr[j]):
                count=count+1
            j=j+1
    return count+1
print(funtion123(5,[1,2,1001,4,3]))
            