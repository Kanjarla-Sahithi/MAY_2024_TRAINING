"""ip:"xyzabcdefklmnopqefgh"
op: 7 """
string=input()
count=1
m=0
for s in range(len(string)-1):
    if ord(string[s])==ord(string[s+1])-1:
        count=count+1
    else:
        if m>count:
            continue
        else:
            m=count
        count=1
if m<count:
    m=count
print(m)
    
        
        
        
