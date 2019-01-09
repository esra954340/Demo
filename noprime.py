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
    if(n>=1):
        print(2)
        count+=1

    i=3
    while(count<n):
        if(isprime(i)):
            count+=1
        i=i+2
        print(i)
  #  print(count)
n=input("enter the no:")
#m=input("enter the no:")

#print(printprime(int(n)))
print(isprime(n))