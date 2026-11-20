class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node 
    def print(self):
        temp=self.top
        print("stack data")
        while temp:
            print(temp.data)
            temp=temp.next
class queue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            dequed_data=temp.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
                print("now queue is empty")
            temp=None
            return dequed_data
        else:
            print("Queue is empty")
    def is_empty(self):
        return self.front is None
    def print(self):
        temp=self.front
        print("queue data")
        while temp:
            print(temp.data,"->")
            temp=temp.next
def revese_queue(q1):
    sta1=stack()
    while not q1.is_empty():
        sta1.push(node(q1.dequeue()))
    sta1.print()
que=queue()
que.enqueue(node(15))
que.enqueue(node(67))
que.enqueue(node(55))
que.enqueue(node(100))
que.enqueue(node(88))
que.print()
revese_queue(que)