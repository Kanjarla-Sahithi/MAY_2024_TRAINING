"""ip:
    15  3  2  7  8  4
    m t  w  th f  s
op:
6
"""

l=[15,3,2,7,8,4]

"""
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if l[i]<l[j]:
            profit=l[j]-l[i]
        if maxi<profit:
            maxi=profit
print(maxi)"""
b=999999999
for i in range(len(l)):
    if a>l[i]:
        a=l[i]
    else:
        profit=l[i]-a
        if maxi<profit:
            maxi=profit
print(maxi)
        
        
        
        
    
    
    


