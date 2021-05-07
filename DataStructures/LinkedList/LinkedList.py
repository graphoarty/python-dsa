from .LinkedListNode import *

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        
        newNode = LinkedListNode(value, self.head)
        self.head = newNode

        if not self.tail == None:
            self.tail = newNode

        return self

    def append(self, value):
        
        newNode = LinkedListNode(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

        self.tail.next = newNode
        self.tail = newNode

        return self

    def find(self, value):
        
        if self.head == None:
            return None

        currentNode = self.head

        while not currentNode == None:

            if currentNode.value == value:
                return currentNode

            currentNode = currentNode.next

        return None

    def delete(self, value):

        if self.head == None:
            return None

        deletedNode = None

        while not self.head == None and self.head.value == value:
            deletedNode = self.head
            self.head = None
            # self.head = self.head.next

        currentNode = self.head

        if not currentNode == None:
            while not currentNode.next == None:
                if currentNode.next.value == value:
                    deletedNode = currentNode.next
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next
            
        if self.tail.value == value:
            self.tail = currentNode

        return deletedNode