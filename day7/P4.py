#Finding Coprimes 
"""n1=4
n2=7
n1l=set()
n2l=set()

for i in range(2,n1):
    if n1%i==0:
        n1l.add(i)
for i in range(2,n2):
    if n2%i==0:
        n2l.add(i)
        
if n1l.intersection(n2l):
    print("Not Prime")
else:
    print("Co Prime")"""


import math
if math.gcd(4,7)==1:
    print("Coprime")
else:
    print("Not CoPrime")



