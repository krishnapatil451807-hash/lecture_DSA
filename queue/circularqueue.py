class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class cqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front # added for circular queue
    def dequeue(self):
        if self.front:# checks at least one node in the queue 
            temp=self.front
            if self.front==self.rear:
                self.front=self.rear=None# updated for circular queue
                print("now queue is empty")
            else:
                self.front=self.front.next
                self.rear.next=self.front # added for circular queue
            temp=None
        else:
            print("Queue is empty")
    def print(self):
        temp=self.front
        print("queue data")
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.front:
                break
que=cqueue()
que.enqueue(node(15))
que.enqueue(node(67))
que.enqueue(node(55))
que.enqueue(node(100))
que.enqueue(node(88))
que.print()
que.dequeue()
que.print()