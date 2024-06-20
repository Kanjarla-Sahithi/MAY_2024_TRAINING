#DFS
def graphtraversal(dic,x):
    stack.append(x)
    for i in dic[x]:
        if i not in stack:
            graphtraversal(dic,i)
            
def allpaths(dic,x,last):
    l.append(x)
    if x==last:
        print(l)
        l.pop()
        return
    for i in dic[x]:
        if i not in l:
            allpaths(dic,i,last)
    l.pop()

def weightedgraph(dic,x,last,s,cost,l):
    l.append(x)
    s+=cost
    if x==last:
        print(l," ",s)
        l.pop()
        return
    for i in dic[x]:
        if i[0] not in l:
            weightedgraph(dic,i[0],last,s,i[1],l)
    l.pop()

def leastCost(dic,key,last,s,cost,l,m):
    l.append(key)
    s+=cost
    if key==last:
        if s<m:
            m=s
        l.pop()
        return m 
    for i in dic[key]:
        if i[0] not in l:
            m=leastCost(dic,i[0],last,s,i[1],l,m)
    l.pop()
    return m


def lowCostpath(dic,key,last,s,cost,l,m,l1):
    l.append(key)
    s+=cost
    if key==last:
        if s<m:
            m=s
            l1=l.copy()
        l.pop()
        return m,l1 
    for i in dic[key]:
        if i[0] not in l:
            m,l1=lowCostpath(dic,i[0],last,s,i[1],l,m,l1)
    l.pop()
    return m,l1
 
    
dic={  5:[7,3],
            7:[5,4,3],
            4:[7,8,2],
            8:[3,4,2],
            3:[5,7,8],
            2:[4,8]
         }
   
"""dic={  5:[(7,1),(3,3)],
            7:[(5,1),(4,4),(3,2)],
            4:[(7,4),(8,2),(2,4)],
            8:[(3,6),(4,2),(2,5)],
            3:[(5,3),(7,2),(8,6)],
            2:[(4,4),(8,5)]
         }"""
stack=[] # list is a global variable so no need to insert in the function
l=[]
last=2
for i in dic:
    allpaths(dic,5,i)
    
    
#graphtraversal(dic,5)
#print("The GraphTraversal is ",stack)
print()
#allpaths(dic,5,last)
s=0
cost=0
res={}
#weightedgraph(dic,5,last,s,cost,l)
#print(lowCostpath(dic,5,last,s,cost,l,99999999999,[]))
#print(leastCost(dic,5,last,s,cost,l,99999999999))




