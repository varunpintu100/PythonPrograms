def code(numlist,leng):
    if len(numlist)==1:
        return 1
    else:
        numlist=sorted(numlist)
        i=int(leng/2)
        j=i+1
        z=numlist[j-1]-numlist[i-1]
        if(z<0):
            z=z*-1
            z=z+1
            return z
        else:
            return z+1
test=int(input())
while(test!=0):
    lt=[]
    leng=int(input())
    lt=list(map(int,input().split(" ")))
    print(code(lt,leng))
    test=test-1