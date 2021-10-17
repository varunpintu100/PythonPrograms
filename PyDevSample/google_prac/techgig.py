def logic(mi,ma):
    low,high=0,0
    ref1,ref2=mi,ma
    if (mi==ma):
        return 0
    else:
        while(ref1!=ma):
            c=0
            for i in range (1,ref1):
                if ref1%i==0:
                    c +=1
            if c==1:
                low=ref1
                break
            else:
                ref1 +=1
        while(ref2!=mi):
            c=0
            for i in range (1,ref2):
                if ref2%i==0:
                    c +=1
            if c==1:
                high=ref2
                break
            else:
                ref2 -=1 
    if high!=0 and low!=0:
        return high-low
    elif high==0 and low==0:
        return -1
    else:
        return 0

if __name__=="__main__":
    for _ in range (int(input())):
        l,r=map(int,input().split(" "))
        print(logic(l,r))