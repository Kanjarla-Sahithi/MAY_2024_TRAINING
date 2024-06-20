"""ip:
    tu5g2k1h8
    g5g8gd6h3
    first bring out unique elements and write the largest even number
op:
    865312 """

s1="tu5g2k18"
s2="g5g8gd6h3"
s=set()
for i in s1:
    if i.isdigit():
        s.add(i)
for i in s2:
    if i.isdigit():
        s.add(i)
l=list(s)
l.sort()
for i in l:
    if int(i) % 2==0:
        es=i
        l.remove(i)
        break
st=""
for i in range(len(l)-1, -1, -1):
    st+=l[i]
st+=es
print(st)
        
        
        
        
        
