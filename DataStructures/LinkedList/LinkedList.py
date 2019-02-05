from .LinkedListNode import *

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        
        newNode = LinkedListNode(value, self.head)
        self.head = newNode

        if not this.tail == None:
            this.tail = newNode

        return self

    def append(self, value):
        
        newNode = LinkedListNode(value)

        if not self.head == None:
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

    