'''
ip:
    3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
op:
    3 - 4
    5 - 1
    4 - 2
    6 - 2
    7 - 2
    1 - 1
    2 - 1
    8 - 2
'''
l=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
"""
count=0
s=set()
for i in l:
    if i in s:
        continue
    for j in range(len(l)):
        if i == l[j]:
            count+=1
    s.add(i)
    print(i ,'-',count)
    count=0 (or)  '''
ip:
    3 5 4 3 6 7 1 2 4 3 3 7 6 8 8

op:

    3 - 4
    5 - 1
    4 - 2
    6 - 2
    7 - 2
    1 - 1
    2 - 1
    8 - 2

'''
l=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
count=0
s=set()
for i in l:
    if i in s:
        continue
    for j in range(len(l)):
        if i == l[j]:
            count+=1
    s.add(i)
    print(i ,'-',count)
    count=0 """
b=[]
for i in l:
    if i not in b:
        b.append(i)
for i in b:
    print(i,"-",l.count(i))

