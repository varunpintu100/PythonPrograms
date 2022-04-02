test=list(map(int,input()))
operations = input()
index,temp,count,length=0,0,0,len(operations)
while count<length:
    if operations[count]=='R':
        index +=1
    elif operations[count]=='L':
        index -=1
    elif operations[count]=='T':
        test[index]+=1
    elif operations[count]=='D':
        test[index]-=1
    else:
        temp=test[index]
        test[index]=test[int(operations[count+1])-1]
        test[int(operations[count+1])-1] = temp
        count+=1
    count+=1
res = int("".join(map(str, test)))
print(res)
        
        