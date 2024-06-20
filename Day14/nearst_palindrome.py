"""
ip: 122
if it is a palindrome print palindrome else print next nearst palindrome
op:131
----------------------------
ip: 1234
op: 1331
--------------------------------
ip: 24
op:33
-------------------
"""

def palindrome(num,rem,rev):
    n=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if n==rev:
        return True
    return False
    
num=1234
rem=0
rev=0
r=0
s1=0
if palindrome(num,rem,rev):
    print("Palindrome")
else:
    if len(str(num))%2==0:
        s1=str(num)[:len(str(num))//2]
        r=s1+s1[::-1]
        if int(r)>num:
            print(r)
        else:
            s1=str(num)[:len(str(num))//2]
            s1=int(s1)+1
            s1=str(s1)
            r=s1+s1[::-1]
            print(r)
    else:
        pass
        
        

        
        
        
        
        
