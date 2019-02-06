from hashlib import md5
from DataStructures.LinkedList.LinkedList import *

# The size of the hashtable is directly proportional to the number of collisions that might occur.
defaultHashTableSize = 32

class HashTable:

    # @param {number} hashTableSize
    def __init__(self, hashTableSize = defaultHashTableSize):

        # Should probably be named HashTableEntry. You get the point.
        self.buckets = [LinkedList() for x in range(0, hashTableSize)]

        # A quick lookup for has() and getKeys().
        self.keys = {}

    # @param {string} key
    # @param {*} value
    def set(self, key, value):

        keyHash = self.hash(key)
        self.keys[key] = keyHash
        bucketLinkedList = self.buckets[keyHash]  

        node = bucketLinkedList.find({key: value})
        
        if node == None:
            bucketLinkedList.append({key: value})
        else:
            node.value.value = value

    # @param {string} key
    # @returns {*}
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

    # @param {string} key
    # @returns {*}
    def delete(self, key):

        keyHash = self.hash(key)
        del self.keys[key]
        bucketLinkedList = self.buckets[keyHash]

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

        return None
    
    # @params {string} key
    # @returns {number}
    def hash(self, key):
        k = 0
        for s in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(s)
        return k % len(self.buckets)

    # @params {string} key
    # @returns {boolean}
    def has(self, key):
        if key in self.keys.keys():
            return True
        else:
            return False

    # @returns {string[]}
    def getKeys(self):
        return list(self.keys.keys())

