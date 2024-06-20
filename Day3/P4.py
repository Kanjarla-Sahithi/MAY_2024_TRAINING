"""ip: 12321
op: check palindrome or not """
def reverse(num,r):
    if num==0:
        return r
    else:
        r=r*10 + num%10
        return reverse(num//10, r)
    
num= int(input())
r=0
rev=reverse(num,r)
if(rev==num):
    print("palindrome")
else:
    print("not palindrome")

