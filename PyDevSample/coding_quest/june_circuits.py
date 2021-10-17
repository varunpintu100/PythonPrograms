def count(h,m):
    count1=0
    if h<12:
            for i in range(0,h+1):
                for j in range(0,60):
                    ang1=(i*60+j)*0.5
                    ang2=(j)*6
                    temp=ang1-ang2
                    if i==h and j==m:
                        if temp<=0:
                            return count1+1
                        else:
                            return count1
                    if temp<=0:
                        count1 +=1
                        break
            return count1
    else:
            h=h-12
            for i in range(0,h+1):
                for j in range(0,60):
                    ang1=(i*60+j)*0.5
                    ang2=(j)*6
                    temp=ang1-ang2
                    if i==h and j==m:
                        if temp<=0:
                            return count1+12
                        else:
                            return count1+11
                    if temp<=0:
                        count1 +=1
                        break
            return count1+11
hours,minu=map(int,input().split(":"))
print(count(hours,minu))    

