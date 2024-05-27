""" ip: 14
op: 17
If the number is prime then print prime number else print next nearest prime"""
def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
n=int(input())
if prime(n) is True:
    print(n)
else:
    while 1:
        if prime(n+1):
            print(n+1)
            break
        else:
            n=n+1
    

        
        
        
