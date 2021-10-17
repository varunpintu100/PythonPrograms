arr=[]
refer=[]
final=[]
sum=[]
for i in range(int(input())):
    p=int(input())
    arr.append(p)
    refer.append(p)
for i in range (1,len(arr)):#this part is insertion sort to arrange the set in ascending order
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key # end of insertion sort 
for i in range(len(arr)):#the sorted array that contains the summed elements s
    if i==0:
        rep=arr[i+1]
        sum.append(rep)
    elif i==(len(arr)-1):
        rep=arr[i-1]
        sum.append(rep)
    else:
        rep=arr[i-1]+arr[i+1]
        sum.append(rep)
for i in range (len(arr)):
    for j in range (len(arr)):
        if refer[i]==arr[j]:
            final.append(sum[j])
print(final)