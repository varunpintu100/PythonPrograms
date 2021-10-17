l=int(input())
lt=[]
lt=list(map(int,input().split(" ")))
if len(lt)%2==0:
    while len(lt)!=0:
        m=max(lt)
        lt.remove(m)
        n=min(lt)
        lt.remove(n)
        print("{}  {}".format(m,n))
else:
    while len(lt)!=1:
        m=max(lt)
        lt.remove(m)
        n=min(lt)
        lt.remove(n)
        print("{}  {}".format(m,n))
    print("{}  {}".format(max(lt),0))
    