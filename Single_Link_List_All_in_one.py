import os
os.system("cls")

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self) -> str:
        return f"node with value == {self.value}"
  
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.lenght=1
        
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.lenght+=1
        return True
    
    def pop(self):
       if self.lenght==0:
           return "Empty list"
       temp,pre=self.head,self.head      
       while temp.next is not None:
            pre=temp
            temp=temp.next
       self.tail=pre
       self.tail.next=None
       self.lenght-=1
       if self.lenght==0:
            self.head,self.tail=None
       return temp
    def prepend(self,value):
        new_Node=Node(value)
        if self.head is None:
            self.head=new_Node
            self.tail=new_Node
            self.lenght=1
        else:
           post=self.head
           self.head=new_Node
           self.head.next=post
           self.lenght+=1
        return new_Node
    
    def pop_first(self):
        if self.lenght==0:
            return "Empty List"
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.lenght-=1
            if self.lenght==0:
                self.tail=None
            return temp
    def get_index(self,index):
        if self.lenght < 0 or index>self.lenght:
            return "index out of bounds"
        temp,get_node=self.head,self.head
        while index>=0:
            get_node=temp
            temp=temp.next
            index-=1
        return get_node
    
    def insert(self,index,value):
        if self.lenght < 0 or index>self.lenght:
            return "index out of bounds"
        if index==0:
            self.prepend(value)
            return True
        temp=self.head
        # better option would be to use get function
        for _ in range(index-1):
            temp=temp.next
        new_Node=Node(value)
        post=temp.next
        temp.next=new_Node
        new_Node.next=post
        self.lenght+=1
        return True
    def set_value(self,index,value):
        if not self.get_index(index):
            return False
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
        return temp
        
    def remove(self,index):
        if self.lenght < 0 or index>=self.lenght:
            return "index out of bounds"
        if index==self.lenght-1:
            return self.pop()
        if index==0:
            return self.pop_first()
        pre_node=self.get_index(index-1)
        node=self.get_index(index)
        pre_node.next=node.next
        self.lenght-=1
        node.next=None
        return node
    
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        after=temp.next
        while after is not None:
            after=after.next
            temp.next=before
            before=temp
            temp=after        
           
         
            
           
            
ll=LinkedList(10)
#ll.printList()
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.printList()
print("@@@@@@@@@@@@@@")
'''
print(ll.pop())
print(ll.pop())
print(ll.pop())
ll.prepend(222)
print("@@@@@@@@@@@@@@")
ll.printList()
print(ll.get_index(1))
#ll.printList()
print("@@@@@@@@@@@@@@")
print(ll.insert(2,420))
ll.printList()

print(ll.set_value(1,1))
ll.printList()
print(ll.remove(0))
'''


ll.reverse()
ll.printList()