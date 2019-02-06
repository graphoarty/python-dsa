from hashlib import md5
from DataStructures.LinkedList.LinkedList import *

defaultHashTableSize = 32

class HashTable:

    def __init__(self, hashTableSize = defaultHashTableSize):
        self.value = None
        self.buckets = [LinkedList() for x in range(0, hashTableSize)]
        self.keys = {}

    def set(self, key, value):

        keyHash = self.hash(key)
        self.keys[key] = keyHash
        bucketLinkedList = self.buckets[keyHash]  

        node = bucketLinkedList.find({key: value})
        # implement linked list here
        if node == None:
            bucketLinkedList.append({key: value})
        else:
            node.value.value = value

    def get(self, key):

        bucketLinkedList = self.buckets[self.hash(key)]

        # custom linkedlist find
        currentNode = bucketLinkedList.head
        while not currentNode == None:
            for k in currentNode.value:
                if k == key:
                    return currentNode.value[k]
            currentNode = currentNode.next

        return None

    def delete(self, key):

        keyHash = self.hash(key);
        del self.keys[key];
        bucketLinkedList = self.buckets[keyHash];

        # custom linkedlist find
        node = None
        currentNode = bucketLinkedList.head
        while not currentNode == None and node == None:
            for k in currentNode.value:
                if k == key:
                    node = currentNode
                    break
            currentNode = currentNode.next

        if not node == None:
            return bucketLinkedList.delete(node.value)

        return None;
    

    # return a number
    def hash(self, key):
        k = 0
        for s in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(s)
        return k % len(self.buckets)
