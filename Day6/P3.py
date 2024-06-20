"""s="the 4quick br$%^ own foENDx j45umps o.ver the lazy dog"
d={}
for i in s:
    if i==" ":
        continue
    if i not in d and i.islower():
        d[i]=1
#print(d)
if len(d)==26:
    print("Perfect")
else:
    print("Nope")"""
s="the 4quick br$%^ own foENDx j45umps o.ver the lazy dog"
d=[0]*26
for i in s:
    if i.islower():
        d[ord(i)-97]=1
print(all(d))
