def inputx(input1,input2):
    l=len(input1)
    s=0
    for i in range(1,l,2):
        s=s+int(input1[i])
        if(s>=input2):
            return str(input1[i-1])
            break
    return str(-1)
input1='a3b2'
input2=7
print(inputx(input1,input2))