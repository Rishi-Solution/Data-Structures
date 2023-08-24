
class PrintLL:
    def __init__(self,llist):
        self.llist=llist
        self.head=llist.head
    def printLL(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=self.llist.next