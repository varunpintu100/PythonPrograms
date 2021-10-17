test=int(input())
i,j,count=0,0,0
lt=[]
lt=list(map(int,input().split(" ")))
for j in range(test):
    key=lt[j]
    i=j-1
    while i>=0 and lt[i]>key:
        lt[i+1]=lt[i]
        i=i-1
        count +=1
    lt[i+1]=key
print(count)
