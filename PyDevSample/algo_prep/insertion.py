def insertion(n):
    l=len(n)
    for j in range(1,l):
        key=n[j] #first step is to initialize a key
        i=j-1  #take i as the preceding number for j 
        while i>-1 and n[i]>key:
            n[i+1]=n[i]
            i=i-1
        n[i+1]=key # after set of iterations the final value gets assigned to final term
    return n 
if __name__=='__main__': 
    lt=[]
    lt=list(map(int,input().split()))
    print(insertion(lt))