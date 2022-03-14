inp=int(input())
lt=[]
lt1=[]
lt=list(map(int,input().split(" ")))
for i in lt:
	lt1.append(lt.count(i))
a=max(lt1)
b=min(lt1)
print(a-b)