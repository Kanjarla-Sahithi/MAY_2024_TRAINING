"""ip "5,3.8,7,5.6,4,2,3"
     op sumofodd=6
          sumofeven = 15
          sumofdecimals = 9.4"""
l=[]
num=[]
decimal=[]
es=0
s=0
for i in range(7):
    l.append(input())
print(l)
for i in l:
    if '.' in i:
        decimal.append(float(i))
    else:
        num.append(int(i))
        s=sum(num)
        for i in num:
            if i%2==0:
                es=es+i
            
            
print(sum(decimal))
print("even sum",es)
print("odd sum",s-es)



