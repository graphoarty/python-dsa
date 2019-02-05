from hashlib import md5

defaultHashTableSize = 32

class HashTable:

    def __init__(self, hashTableSize = defaultHashTableSize):
        self.value = None
        self.buckets = [{} for x in range(0, hashTableSize)]
        self.keys = {}

    def set(self, key, value):

        keyHash = self.hash(key)
        self.keys[key] = keyHash
        bucketLinkedList = self.buckets[keyHash]  

        # implement linked list here
        bucketLinkedList[key] = value

    def get(self, key):

        bucketLinkedList = self.buckets[self.hash(key)]
        return bucketLinkedList[key]

    # hash to return a number
    def hash(self, key):
        k = 0
        for s in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(s)
        return k % len(self.buckets)
