ref=int(input())
eve=[]
odd=[]
if 2<=ref<=3:
    print("NO SOLUTION")
elif ref==1:
    print('1')
else:
    for i in range(1,ref+1):
        if i%2==0:
            print(i,end=' ')
    for i in range(1,ref+1):
        if i%2!=0:
            print(i,end=' ')
        