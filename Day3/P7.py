""" ip: 5
op:
      * * * * *
      * 1 2 3 *
      * 4 5 6 *
      * 7 8 9 *
      * * * * *
"""
"""n=5
x=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(x,end=" ")
            x=x+1
    print()
------------------------------------------------------"""
""" ip =4
  op:
      - - - - a - - - -
      - - - a b a - - -
      - - a b c b a- -
      - a b c d c b a -"""
n=int(input())
ch=97
for i in range(n):
    for j in range(n-1,0,-1):
        print("-")
    for k in range(n):
        print(chr(ch),end="")
        ch=ch+1
    ch=ch-1
    for m in range(n):
        print(chr(ch),end="")
        ch=ch-1
    for j in range(n-1,0,-1):
        print("-")
    print()
    ch=97
        
    


    
