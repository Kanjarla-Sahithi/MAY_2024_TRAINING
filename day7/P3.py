"""n=16
k=1
for i in range(n,-1,-1):
    if n%i==0:
        k-=1
        if k==0:
            print(i)
            break"""
def factors(k,n,i):
    if k==0:
        return i+1
    if n%i==0:
        k-=1
    return factors(k,n,i-1)
n=12
print(factors(2,n,n))
    
    
    
    
