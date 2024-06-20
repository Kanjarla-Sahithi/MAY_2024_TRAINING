def fun1(x,a,b,es,os):
    if x==len(a):
        return (es,os)
    if a[x] %2==0:
        es=es+a[x]
    if b[x] %2!=0:
        os=os+b[x]
    return fun1(x+1, a,b,es, os)

a=[3,8,5,4,3]
b=[5,0,9,3,2]
es=0
os=0
print(fun1(0,a,b,es,os))
