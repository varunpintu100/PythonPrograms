import time
start_time=time.time()
def countdown(n):
    if n==0:
        print("Done")
        return
    else:
        print(n ,end=" ")
        countdown(n-1)
countdown(int(input()))
print("%s "%(time.time() - start_time))
