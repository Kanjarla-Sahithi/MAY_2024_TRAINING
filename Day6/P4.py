""" length of longest substring without repeating character
ip:  "abfgresagtyuiofde"
op: 12
( from r to d) """
"""s="abfgresaztyuiofde"
l=[]
m=0

for i in range(len(s)):
    l.append(s[i])
    for j in range(i+1,len(s)):
        if s[j] not in l:
            l.append(s[j])
        else:
            m=max(len(l),m)
            l=[]
            break
    l=[]
print(m)"""
string="abfgresaztyuiofde"
d={}
s=""
m,i=0,0
while i<len(string):
      while i<len(string):
          if string[i] not in s:
              s=s+string[i]
              d[s[i]]=i
          else:
              if len(s)>m:
                  m=len(s)
              s=""
              break
          i=i+1
      i=d[s[i]]+1
print(m)
        
    



    
