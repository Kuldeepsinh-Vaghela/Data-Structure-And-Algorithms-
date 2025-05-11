class Node():
    def __init__(self,value=None):
        self.value  = value
        self.next = None

class Slinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self,value,location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == -1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                number = 0
                while number < location-1:
                    tempnode = tempnode.next
                    number+=1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
    def traverseSLL(self):
        if self.head is None:
            print("There is no singly linked list")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node= node.next
    def searchSLL(self,nodevalue):
        if self.head is None:
            print("There is no singly linked list")
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                node = node.next
            return "The value does not exist"
    def deleteNode(self,location):
        if self.head is None:
            print("There is no singly linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                indx = 0
                while indx < location -1:
                    tempnode = tempnode.next
                    indx += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next
    def deleteentireSLL(self):
        if self.head is None:
            print("There is no singly linked list")
        else:
            self.head = None
            self.tail = None
                
singlelinkedlist = Slinkedlist()
singlelinkedlist.insertSLL(1,-1)
singlelinkedlist.insertSLL(2,-1)
singlelinkedlist.insertSLL(3,-1)
singlelinkedlist.insertSLL(4,-1)
singlelinkedlist.insertSLL(0,0)
singlelinkedlist.insertSLL(10,2)
print([node.value for node in singlelinkedlist] )
singlelinkedlist.traverseSLL()
print([node.value for node in singlelinkedlist] )
singlelinkedlist.deleteNode(1)
print([node.value for node in singlelinkedlist] )
singlelinkedlist.deleteentireSLL()
print([node.value for node in singlelinkedlist] )

#CIRCULAR SINGLY LINKED LIST
 
class CircularSlinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    def createCSLL(self,nvalue):
        node = Node(nvalue)
        node.next = node
        self.head = node
        self.tail = node
    def insertCSLL(self, value, location):
        if self.head is None:
            return 'the head reference is not given'
        else:
            newnode = Node(value)
            if location == 0:
                newnode.next = self.head
                self.head = newnode
                self.tail.next = newnode
            elif location == -1:
                newnode.next = self.tail.next
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                indx = 0
                while indx < location -1:
                    tempnode = tempnode.next
                    indx += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
    def traverseCSLL(self):
        if self.head is None:
            return 'there is no element to traverse'
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break
    def searchCSLL(self,nodevalue):
        if self.head is None:
            return "There are no elememnts in linked list"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodevalue:
                    return tempnode.value
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    return "The provdied element is not present in linked list"
    def deleteCSLL(self,location):
        if self.head is None:
            return "There is no node in linked list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempnode = self.head
                    while tempnode is not None:
                        if tempnode.next == self.tail:
                            break
                        tempnode = tempnode.next
                    tempnode.next = self.head
                    self.tail = tempnode
            else:
                tempnode = self.head
                indx = 0
                while indx < location -1:
                    tempnode = tempnode.next
                    indx+=1
                nextnode = tempnode.next
                tempnode.next = nextnode.next
    def deleteentireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

                  

circularsingularLinkedList = CircularSlinkedlist()
circularsingularLinkedList.createCSLL(1)
print([node.value for node in circularsingularLinkedList])
circularsingularLinkedList.insertCSLL(2, -1)
circularsingularLinkedList.insertCSLL(3, -1)
circularsingularLinkedList.insertCSLL(4, -1)
circularsingularLinkedList.insertCSLL(100, -1)
print([node.value for node in circularsingularLinkedList])
circularsingularLinkedList.traverseCSLL()
print(circularsingularLinkedList.searchCSLL(100))
print([node.value for node in circularsingularLinkedList])
circularsingularLinkedList.deleteCSLL(4)
print([node.value for node in circularsingularLinkedList])
circularsingularLinkedList.deleteentireCSLL()
print([node.value for node in circularsingularLinkedList])

# Doubly Linked lists

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # creating a doubly linked list with 1 node
    def createDLL(self,nodevalue):
        node = Node(nodevalue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
    def insertDLL(self,nodevalue,location):
        if self.head is None:
            print("The head referece is not given")
        else:
            newnode = Node(nodevalue)
            if location == 0:
                newnode.next = self.head
                newnode.prev = None
                self.head.prev = newnode
                self.head = newnode
            elif location == -1:
                newnode.prev = self.tail
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else: 
                tempnode = self.head
                indx = 0
                while indx < location-1:
                    tempnode = tempnode.next
                    indx += 1
                nextnode = tempnode.next
                newnode.next = nextnode
                newnode.prev = tempnode
                nextnode.prev = newnode
                tempnode.next = newnode
            
                

                
                


doublyLinkedlist = DoublyLinkedlist()
doublyLinkedlist.createDLL(0)
doublyLinkedlist.insertDLL(1,-1)
doublyLinkedlist.insertDLL(2,-1)
doublyLinkedlist.insertDLL(3,-1)
doublyLinkedlist.insertDLL(4,-1)
print([node.value for node in doublyLinkedlist])