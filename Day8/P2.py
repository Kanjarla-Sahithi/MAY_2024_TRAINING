"""ip: "hello:5438,car:214,book:8799,apple:2187""
op: oaxp"""

l = dict(item.split(':') for item in input().split(','))
for key,value in l.items():
    length=len(key)
    f=0
    if str(length) in value:
        print(key[length-1],end="")
        f=1
        continue
    for i in range(length-1,0,-1):
        if str(i) in value:
            print(key[i-1],end="")
            f=1
            break
    if f==0:
        print("x",end="")
        continue

