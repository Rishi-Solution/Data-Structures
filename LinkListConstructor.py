class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.lenght=1
        
class printLL:
    def __init__(self,linkList) -> None:
        self.linkList=linkList
    def printList(self):
        temp=self.linkList.head        
        while temp is not None:
            print(temp.value)
            temp=temp.next
ll=LinkedList(10)
prin=printLL(ll)
prin.printList()
            


    