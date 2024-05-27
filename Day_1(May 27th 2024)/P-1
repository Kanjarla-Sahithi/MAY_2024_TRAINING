"""input : list1 = 2 5 7 9 list2 = 1 3 6 7 10 13
op: 1, 2, 3, 5, 6, 7, 7, 9, 10, 13] """
a = [1,5,7,9]
b = [2,3,6,7,10,13]
c=[ ]
i,j=0,0
while(i<len(a) and j<len(b)):
    if (a[i] < b[j]):
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
"""while j<len(b):
    c.append(b[j])
    j=j+1
while i<len(a):
    c.append(a[i])
    i=i+1 (or) """

if(j<len(b)):
    c.extend(b[j:])
if(i<len(a)):
    c.extend(a[i:]) 
print(c)
    

    
    
    

