class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = None

    def printlst(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
# if __name__ == '__main__':
lst = linkedList()
lst.head = Node(1)
second = Node(2)
third = Node(3)
lst.head.next = second
second.next = third

lst.printlst()