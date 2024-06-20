"""ip :
           7
           0 5 3 6 7 2 1
    op: 4"""
"""n=7
s=0
l=[0,5,3,6,4,2,1]
for i in range(n+1):
    s=s+i
for i in l:
    s=s-i
print(s)"""
leetcode: 268
n=7
l=[0,5,3,6,4,2,1]
b=sum(l)
n=(n*(n+1))//2
print(n-b)

