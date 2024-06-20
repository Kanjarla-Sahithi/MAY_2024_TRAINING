"""
    ip: [4,8,14,22,37,68]
    all the elements in the array are non prime numbers and in the increasing order
    find the largest prime number b/w 2,2 numbers and make the sum of the of all primes
"""
l=list(map(int,input().split()))
#l=[14,16,20,22]
def isprime(j):
    for i in range(2, j//2+1):
        if j%i==0:
            return 0
    return j
newl=[]
for i in range(len(l)-1):
    m=0
    for j in range(l[i],l[i+1]):
        m=max(isprime(j),m)
    newl.append(m)
print(newl)
print(sum(newl))



        
    
    

