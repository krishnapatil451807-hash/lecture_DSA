class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            poped_data=temp.data
            print("poed element",temp.data)
            self.top=self.top.next
            temp=None
            return poped_data

    
    def print(self):
        temp=self.top
        print("stack data")
        while temp:
            print(temp.data)
            temp=temp.next
class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def print(self):
            temp=self.front
            print("queue data")
            while temp:
                print(temp.data,"->")
                temp=temp.next
def reverse_stack(s1):
    que=queue()
    while not  s1.isempty():
        que.enqueue(node(s1.pop()))
    que.print()
sta=stack()
sta.push(node(10))
sta.push(node(100))
sta.push(node(45))
sta.push(node(87))
sta.push(node(50))
sta.print()
reverse_stack(sta)
