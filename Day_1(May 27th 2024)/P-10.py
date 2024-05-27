'''
inp:
    asd8728#*^A
op:
    if valid then -1

------------------------
ip:
123456789

op:
    3
-----------------------------
ip:
    ab

op:
    6
----------------------
'''
s=input("enter a password")
caps,small,num,sp=[],[],[],[]
char=-1

for i in s:
    if i.isupper():
        caps.append(i)
    elif i.islower():
        small.append(i)
    elif i.isdigit():
        num.append(i)
    else:
        sp.append(i)
if len(s)>=8 and len(caps)!=0 and len(small)!=0 and len(num)!=0 and len(sp)!=0:
    print(char)
    
elif len(s)>8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(small)==0:
        char+=1    
    if len(num)==0:
        char+=1
    if len(sp)==0:
        char+=1
        
elif len(s)<8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(small)==0:
        char+=1    
    if len(num)==0:
        char+=1
    if len(sp)==0:
        char+=1
    if char+len(s)<8:
        char=char+(8-len(s)-char)
    print(char)    
