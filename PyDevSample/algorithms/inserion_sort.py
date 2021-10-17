count=0
arr=list(map(int,input().split(" ")))
for j in range(0,len(arr)):
    key=arr[j]
    i=j-1
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        i=i-1
    arr[i+1]=key
print(arr)