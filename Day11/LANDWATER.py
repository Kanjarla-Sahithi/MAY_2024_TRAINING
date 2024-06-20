l=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=len(l)
count=0
c=0
def fun(l,i,j,n,c):
    if l[i][j]==0:
        return c
    
    if l[i][j]==1:
        l[i][j]=0
        c=c+1
    
    if i>0:
        c=fun(l,i-1,j,n,c) 
    if i<n-1:
        c=fun(l,i+1,j,n,c)   
    if j>0:
        c=fun(l,i,j-1,n,c) 
    if j<n-1:
        c=fun(l,i,j+1,n,c)
    return c
res=[]

for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
            res.append(fun(l,i,j,n,0))
print(max(res))
print(count)
            
