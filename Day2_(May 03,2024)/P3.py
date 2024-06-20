def fun(n,x,s):
    if n>x:
        return s
    if x%2==0:
        s=s+x
    return fun(n,x+1,s)
        
n=10
print(fun(n,1,0))
    