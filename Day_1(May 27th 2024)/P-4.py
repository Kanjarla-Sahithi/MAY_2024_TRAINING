""" ip:
          f46feLK9y56u#@&56hIjbn6KJhA
"""
string = "f46feLK9y56u#@&56hIjbn6KJhA"
lv,uv,lc,uc,d,s=0,0,0,0,0,0
"""for i in string:
    if i.islower():
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            lv=lv+1
        else:
            lc=lc+1
    elif i.isupper():
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            uv=uv+1
        else:
            uc=uc+1
    elif i.isdigit():
        d=d+1
    elif (not i.isalnum()):
        s=s+1
    (or) else:
        s=s+1
"""
for i in string:
    if i.islower():
        if (i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif i.isupper():
        if (i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif i.isdigit():
        d=d+1
    elif (not i.isalnum()):
        s=s+1
   
print("lv - ",lv)
print("lc - ",lc)
print("uv - ",uv)
print("uc - ",uc)
print("d - ",d)
print("s - ",s)

            
            
        
