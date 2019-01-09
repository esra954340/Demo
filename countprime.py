import math
def isprime(n):
    flag=True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            flag=False
            break
    return flag
def printprime(n):
    count=0
    if(n>=2):
        count+=1
    for i in range(3,n+1,2):
        if(isprime(i)):
            count+=1
    print(count)
n=input("enter the no:")
#print(isprime(int(n)))
printprime(n)