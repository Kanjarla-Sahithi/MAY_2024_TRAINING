"""ip:  [2,3,1,3,4,3,2]
op:  [[2,3,1,4],[3,2],[3]]
-----------------------------------
"""
l=[2,3,5,1,2,4,9,1,2,4]
r=[]
res=[]
while l:
    for i in l:
        if i not in r:
            r.append(i)
    for i in r:
        l.remove(i)
    res.append(r)
    r=[]
print(res)

            
