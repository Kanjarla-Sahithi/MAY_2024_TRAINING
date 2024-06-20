"""Add all the digits of the number and check the sum value if prime print the n value if not increment and check"""    

def check(n):
    x=sum(n)
    while x>10:
        x=sum(x)
    if x in [2,3,5,7]:
        print(n)
    else:
        check(n+1)
        
def sum(n):
    rem=0
    s=0
    while n:
        rem=n%10
        s=s+rem
        n=n//10
    return s
n=int(input())
check(n)


    


    

