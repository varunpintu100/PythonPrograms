import math
def equationroots(a,b,c):
    dis=(4*b*b)-(4*c)
    sqrt_val=math.sqrt(abs(dis))
    if dis>0: 
        sol1=(2*b + sqrt_val)/2
        sol2=(2*b - sqrt_val)/2 
    elif dis==0:
        sol1=(2*b + sqrt_val)/2 
        sol2=(2*b - sqrt_val)/2
    else:
        return False
    if sol1.is_integer() and sol2.is_integer():
        return True
    elif sol1 and sol2 <0:
        return False
if __name__ == '__main__':
    a=1
    flag=False
    out=0
    test=int(input())
    for i in range (test):
        out=0
        st=input()
        b,c=st.split("  ")
        b=int(b)
        c=int(c)
        for x in range (b,c+1):
            for y in range (b,c+1):
                flag=equationroots(a,x,y)
                if flag:
                    out +=1
        print(out)
        