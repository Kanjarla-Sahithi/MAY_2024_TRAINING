"""
The input is no of queries
ip: 7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch

1 means insert the word
2 means search for the word
3 means search for the prefix word

op:
True
False
True
-------------------------------------------------------------
ip: 5
1 word
1 word
3 wo
4 word
2 word
-------------------------------------------------------------
"""
queries=int(input())
l=[]
res=[]
for i in range(queries):
    n=int(input("Enter the number:"))
    word=input("Enter the word:")
    if n==1:
        if word not in l:
            l.append(word)
    elif n==2:
        if word in l:
            res.append("True")
        else:
            res.append("False")
    elif n==3:
        c=0
        w=len(word)
        for i in l:
            if word==i[:w]:
                c=c+1
                res.append(c)       
    elif n==4:
        l.remove(word)
for i in l:
    print(i)
for i in res:
    print(i)
            
                
        

