test=int(input())
lt=[]
su=0
for i in range(1,test+1):
    lt.append(i)    
    su=su+i
if su%2!=0:
    print("NO")
else:
    print("YES")
print(lt)