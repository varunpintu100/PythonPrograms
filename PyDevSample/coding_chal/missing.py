test=int(input())
sum1,sum2=0,0
lt=[]
lt=list(map(int,input().split(' ')))
for i in range(len(lt)):
    sum1=sum1+lt[i]
for i in range(1,test+1):
    sum2=sum2+i
print(sum2-sum1)