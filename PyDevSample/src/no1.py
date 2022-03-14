test=int(input())
lt=list(map(int,input().split(',')))
ad=int(input())
lt=sorted(lt)
lt1=[]
s,temp=0,0
count=True
for i in range(0,test):
    if(lt[i]==ad):
        return lt[i]
        break
    else:
        for j in range(i+1,test-1):
            s=s+lt[i]+lt[j]
            if(s>=ad):
                lt1.append(s)
                temp=0
                for x in range(0,j):
                    temp=s-lt[x]
                if(temp>=ad):
                    lt1.append(temp)
                count=False
                break
if count:
    return 0
else:
    lt1=sorted(lt1)
    return lt1[0]