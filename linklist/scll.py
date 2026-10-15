class node:
    def __init__(self,value):
        self.data=value
        self.next=None
        pass
class scll:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next !=self.head):
                temp=temp.next
            temp.next=new_node
        new_node.next=self.head
    def insert(self,new_node,pos):
        if pos==1:
            temp=self.head
            while temp.next != self.head:
                    temp=temp.next
                    p+=1
            self.head=new_node
            temp=self.head
        else:
            p=1
            temp=self.head
            while(p!=pos-1 and temp!=self.head):
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
            while temp.next!=self.head: # find the last node
                temp=temp.next 
            temp.next=self.head
        else:
            while temp and temp.data!=value:
                pre=temp
                temp=temp.next
            if temp==self.head:
                print("value is not present ")
                return
            pre.next=temp.next
            temp=None
    def print(self):
            print()
            print("list elements: ")
            temp=self.head
            while(True):
                print(temp.data,end=" ")
                temp=temp.next
                if temp==self.head:
                    break
list1=scll()
n1=node(10) 
n2=node(20)  
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
# list1.print()
list1.insert(node(45),4)
list1.delete(40)
list1.print()