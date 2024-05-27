"""ip : aaabbaaaaddd
    op: a3b2a4d3"""
string="aaabbaaaaddddb"
res=""
count=1
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        count+=1
    else:
        res=res+string[i]+str(count)
        count=1
res=res+string[i+1]
res=res+str(count)

print(res)

    
        
        





