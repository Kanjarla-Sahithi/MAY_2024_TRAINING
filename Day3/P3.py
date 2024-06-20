"""ip: 3
        xyz
        pqr
        abc
        "yraxpazr"
    op: yes
-------------------------------
ip: 4
    abcd
    xyze
    pqrw
    stuv
    "cyptdzsayq"
op: no
---------------------------------"""
def m(matrix,s):
    for i in range(len(s)):
        if s[i] not in matrix[i%n]:
            return 'no'
        matrix[i].remove(s[i])
    return 'yes'
n=int(input("Enter a size of matrix:"))
matrix = []
s=input("Enter the string: ")
for i in range(n): 
    l =[] 
    for j in range(n):
         l.append(list(input()))
    matrix.append(l)
print("The matrix is:", matrix)
print(m(matrix,s))


