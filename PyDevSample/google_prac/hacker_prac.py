def checkPrime(N):
    count = 0
    i=1
    while i*i<=N:
        if N%i==0:
            if i*i==N:
                count +=1
        else:
            count +=2
        i +=1
    if count == 2:
        print("is prime number")
    else:
        print('not a prime number')
n=int(input())
checkPrime(n)       