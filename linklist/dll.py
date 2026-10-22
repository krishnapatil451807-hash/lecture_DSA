#doublly linear linked list 
class node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
class dll:
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
            new_node.prev=temp
    def insert(self,new_node,pos):
        if pos==1:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        else:
            p=1
            temp=self.head
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            if temp.next:
                temp.next.prev=new_node
            new_node.prev=temp
            new_node.next=temp.next
            temp.next=new_node

    def delete(self,value):
        temp=self.head
        if temp is None:
            print("List is empty")
            return
        if temp.data==value:
            self.head=self.head.next
            self.head.prev=None
        else:
            while temp and temp.data!=value:
                temp=temp.next
            if temp==None:
                print("value is not present ")
                return
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.prev
                temp=None
    def reverse(self):
       temp=self.head
       print("/n list element i nreverse order ",end=" ")
       while temp.next:
           temp=temp.next
       while temp:
           print(temp.data,end=" ")
           temp=temp.prev
    # count the occurance of the a given number 
    def count_occur(self,data):
        temp=self.head
        count=0
        while temp.next:
            if temp.data==data:
                count +=1
            temp=temp.next
        print("data",data,"APPEARS",count)

    # def findmid_del(self):
    #     temp=temp1=self.head
    #     while temp1 and temp1.next:
    #         prev=temp
    #         temp=temp.next
    #         temp1=temp1.next.next
    #     print("middle node:", temp.data)
    #     prev.next=temp.next
    #     temp=None
    # def delfirst_last(self):
    #     temp1=self.head
    #     temp1=None
    #     prev=None
    #     temp=self.head=self.head.next
    #     while(temp.next):
    #         prev=temp
    #         temp=temp.next
    #     prev.next=None
    #     temp=None
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
list1=dll()
n1=node(10) 
n2=node(20)  
list1.append(n1)
list1.append(n2)
list1.append(node(30))
list1.append(node(40))
list1.append(node(7))
# list1.print()
list1.insert(node(80),1)
list1.print()
# list1.delete(7)
list1.reverse()