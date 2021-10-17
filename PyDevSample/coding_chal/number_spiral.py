test=int(input())
high=0
for i in range(test):
    rows,column=map(int,input().split(" "))
    high=max(rows,column)
    temp=high*high-(high-1)
    if rows>column:
        if rows%2==0:
            temp=temp+1*(rows-column)
            print(temp)
        else:
            temp=temp-1*(rows-column)
            print(temp)
    else:
        if column%2==0:
            temp=temp-1*(column-rows)
            print(temp)
        else:
            temp=temp+1*(column-rows)
            print(temp)  