number=int(input())
count=0
test=input().strip(" ")
lt=['a','e','i','o','u','A','E','I','O','U']
for i in range(0,len(test)):
    if test[i] in lt:
        count=count+1
count=number-count
print(count)