""" ip placements
"""
s='School'
res=""
for i in s:
    if i in 'aeiouAEIOU':
        res=res+i.upper()
    else:
        res=res+i.lower()
print(res)
        
        
            
            
