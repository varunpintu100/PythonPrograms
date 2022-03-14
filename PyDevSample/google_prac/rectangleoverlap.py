def functn(p1,p2,p3,p4):
    if(p1[0]+p2[0]>p3[0]+p4[0] and p1[1]+p2[1]>p3[1]+p4[1]):
        return("not intersecting")
    else:
        return("intersecting")   
if __name__=='__main__':
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p1=list(map(int,input().split(",")))
    p2=list(map(int,input().split(",")))
    p3=list(map(int,input().split(",")))
    p4=list(map(int,input().split(",")))
print(functn(p1,p2,p3,p4))
