#We canot perform binary search in linked list because there is no indexing for linked list
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def addback(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next

    def addfront(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            newnode=node(data)
            self.head.prev=node(data)
            newnode.next=self.head
            self.head=newnode

    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="<=>")
            t=t.next

    def reverse_display(self):
        t=self.tail
        while(t!=None):
            print(t.data, end="<-->")
            t=t.prev

    def linearsearch(self,key):
        if self.head==None:
            return "List is empty"
        else:
            h=self.head
            t=self.tail
            while t!=h and t.next!=h :
                if h.data==key:
                    return "found"
                elif t.data==key:
                    return "found"
                else:
                    h=h.next
                    t=t.prev
                if h.data==t.data:
                    return "found"
            return "notfound"

    def evenoddlen(self):
        if self.head==None:
            return "List is empty"
        else:
            h=self.head
            t=self.tail
            c=0
            while t!=h and t.next!=h :
                c+=2
                t=t.prev
                h=h.next
            if t==h:
                c+=1
            if c%2==0:
                return "Even"
            else:
                return "Odd"

    def ispalindrome(self):
        if self.head==None:
            return "palindrome"
        else:
            h=self.head
            t=self.tail
            while t!=h and t.next!=h :
                if h.data!=t.data:
                    return "not palindrome"
                h=h.next
                t=t.prev
        return "palindrome"

    def splitting(self):
        if self.head==None:
            return "Empty list"
        else:
            slow=self.head
            fast=self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            tp=self.head
            t=slow.prev
            self.tail.next=tp
            tp.prev=self.tail
            slow.prev.next=None
            slow.prev=None
            self.head=slow
            self.tail=t

    def swapeven(self):
        t1=self.head
        t2=t1.next
        t3=t2.next
        while t3:
            if t1==self.head:
                t1.next=t3
                t3.prev=t1
                t2.prev=None
                t2.next=t1
                t1.prev=t2
                self.head=t2
                
                t1=t1.prev
                t2=t2.next

            else:
                t1.next=t3
                t3.prev=t1
                t2.next=t1
                t1.prev.next=t2
                t2.prev=t1.prev
                t1.prev=t2
                t1=t1.pev
                t2=t2.next

            t1=t1.next.next
            t2=t2.next.next
            t3=t3.next.next
        if t3==None:
            t1.next=t3
            t2.next=t1
            t1.prev.next=t2
            t2.prev=t1.prev
            t1.prev=t2
            self.tail=t1

    def sumcntprime(self,t,c):
        if t==None:
            return c
        def isprime(s,n):
            if s>(n//2)+1:
                return 1
            if n%s==0:
                return 0
            return isprime(s+1,n)
        if(isprime(2,t.data)):
            c=c+1
    return self.pr(t.next,c)
        
            
l=[1,2,3,4,5]
l1=[1,2,3,4,5,6,7,8,9,10]
#obj=dll()
#obj1=dll()
obj2=dll()
'''for i in l:
    obj.addfront(i)
obj.display()
print()
for i in l:
    obj1.addback(i)
print()'''
for i in l1:
    obj2.addback(i)
#obj2.display()
#obj2.reverse_display()
#print(obj2.linearsearch(7))
#print(obj2.evenoddlen())
#print(obj2.ispalindrome())
#obj2.splitting()
print()
#obj2.reverse_display()
obj2.display()
#obj2.swapeven()
print(obj2.sumcntprime())

"""s="(([{}]))"
o=dll()
for i in s:
    o.addback()"""





