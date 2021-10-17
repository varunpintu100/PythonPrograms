test=int(input())
print(test,end=' ')
while test>1:
    if (test%2==0):
        test=test/2
    else:
        test=(test*3)+1
    print(int(test),end=' ')