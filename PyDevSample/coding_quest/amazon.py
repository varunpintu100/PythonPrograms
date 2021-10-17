import math
def deliveryPlan(allocations,deliveries):
    i,j=0,0
    ref=[]
    op=[]
    for i in allocations:
        l,r=map(int,i)
        res=math.sqrt(pow(l,2)+pow(r,2))
        ref.append(res)
    for j in range(0,len(ref)):
        key=ref[j]
        i=j-1
        while i>=0 and ref[i]>key:
            ref[i+1]=ref[i]
            allocations[i+1],allocations[i]=allocations[i],allocations[i+1]
            i=i-1
        ref[i+1]=key
    for j in range(deliveries):
        op.append(allocations[j])
    return op
alli=[[1,2],[3,4],[1,-1]]
deli=2
print(deliveryPlan(alli,deli))