from LinkListConstructor import Node,LinkedList,printLL

class Append:
    def __init__(self,value,link_list) -> None:
        newNode=Node(value)
        self.link_list=link_list
        self.link_list.tail=newNode
                
    def append(self):
        pass
        