"""ip=7856
     op=2"""

n=35721
c=0
while n:
    if (n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)
