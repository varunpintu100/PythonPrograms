ref=input()
count,max1=0,0
for i in range(len(ref)-1):
    if ref[i]==ref[i+1]:
        count +=1
        if count>=max1:
            max1=count
    else:
        count=0
print(max1+1)
    