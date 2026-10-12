#singly linear linked list 
class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def insert(self,new_node,pos):
        if pos==1:
            self.head=new_node
        else:
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
    def delete(self,value):
        temp=self.head
        pre=None
        if temp is None:
            print("List is empty")
            return
        if temp.data==value:
            self.head=self.head.next
        else:
            while temp and temp.data!=value:
                pre=temp
                temp=temp.next
            if temp==None:
                print("value is not present ")
                return
            pre.next=temp.next
            temp=None
    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev
    def findmid_del(self):
        temp=temp1=self.head
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("middle node:", temp.data)
        prev.next=temp.next
        temp=None
    def delfirst_last(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list1=sll()
n1=node(10) 
n2=node(20)  
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
# list1.print()
# list1.insert(node(45),2)
# list1.insert(node(50),5)
# list1.print()
# list1.delete(40)
list1.append(node(40))
list1.append(node(50))
list1.append(node(45))
# list1.reverse()
# list1.findmid_del()
list1.delfirst_last()
list1.print()