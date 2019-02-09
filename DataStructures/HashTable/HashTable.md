## Hash Table

Okay, so hey guys. My name is Quinston and in this video, we are going to talk about the Hash Table and learn how to code one. The Hash Table is a data structure that is used to store data in the form of key-value pairs. The data that is already stored in the Hash Table can be fetched by using the key as a reference. This is why Hash Tables are commonly used as look-up table data structures because they are really fast and reliable when storing key-value pairs where quick look-up is required. 

Before we get into the tutorial, I would really like it if you subscribe to the channel and consider supporting it. All of the content that I produce here is free and I would like to spend more time creating it. Your contribution will go a long way in making sure that the goal is achieved. Links to support the channel are in the description. Let’s go.

The hash table is usually an n-dimensional array. Particularly, in our case, we are going to consider a hash table that is a 1-dimensional array. The way the process of filling up the hash table with key-value pairs works is very interesting. The function that fills up the table is called a set. It takes the key and passes it through a hash function. This hash function is special in the sense that it returns a number. Obviously, you have to make the hash function return a number. This does not happen automatically. Also, it’s not just any number but it’s a number that is actually in the range of 0 and the length of the hash table. Our hash function basically returns the index of where our key-value pair will actually be stored.

There is a caveat to this though. The size of the hash table is not infinite as you will soon find out. What if the hash function returns the same index for two different key-value pairs. Which of the two key-value pairs will be given a spot in the hash table? The phenomenon that would occur in this case is called a collision and collisions need to be dealt with. There are many different ways of dealing with collisions in a hash table but the one which we going to use in our code is called Chaining. Particularly, chaining implemented with a linked list. Just to be clear, I am assuming that you already know what a linked list is and how it works.

The idea here is that each of the buckets or cells of the hash table are actually full-fledged linked lists. When you store a key-value pair now in the hash table, instead of the key-value pair being stored directly inside the cell, it is actually being appended to a linked list which in-turn lives inside the cell. It’s not just the value that’s being stored, but the key-value pair is treated as a unit and appended as a whole towards the end of the linked list. There is a reason for this.

If there are multiple key-value pairs appended to a linked list in a particular cell of the hash table, how would you know which value was actually requested? You literally have to traverse the linked list one by one and test the keys if they match. If the search key matches the key-value pair inside the linked list, we have found our value. It’s very interesting to see the hash table resorting at the mercy of the linked list in this case. 

A better hash function is always going to cause fewer collisions. A bigger table is again going to cause fewer collisions. Let’s take a look at the code.

Let's start with the import statements. The first thing that we import is the hash function that we will be using generate our own custom hash function. We import md5 from hashlib. Next, we are importing the Linked List data structure that we require to properly implement the hash table. No, we are not faking anything here. I actually implemented the Linked List for the purposes of this video. You can check that out in the full code source in the description below.

```python
from hashlib import md5
from DataStructures.LinkedList.LinkedList import *
```

The defaultHashTableSize is the default size of the hash table if there was no explicit size passed in while constructing the hash table. The default size is kept to 32.

```python
defaultHashTableSize = 32
```

Next, we define our hash table class. Once thing that I want to mention here is that, yes, we could have done all of the implementations without actually defining a class and importing the linked list but I don’t think it would have done justice. The beauty of software engineering where code comes together like building blocks is just majestic. 

```python
class HashTable:
```

The constructor, with no surprise, takes the parameter of the hash table size and as we said previously, if no size was explicitly passed, the default size is assumed. Two member variables are defined in the contstructor. The first one is our hash table itself, which is called buckets and the other one is keys. Buckets is defined as an array which is of the length of the value of hashTableSize. This is becuase the buckets array is our 1-dimensional hash table. The keys member variable is defined as an empty dictionary. All of the reason that keys exists can be implemented without actually using keys, but this just provides a quick look up for the functions has() and getKeys() which will be implemented later. Yes, keys might as well be another hash table but lets not get adventurous.  

```python
# @param {number} hashTableSize
    def __init__(self, hashTableSize = defaultHashTableSize):

        # Should probably be named HashTableEntry. You get the point.
        self.buckets = [LinkedList() for x in range(0, hashTableSize)]

        # A quick lookup for has() and getKeys().
        self.keys = {}
```
The most important function or method, whatever you prefer, here is the set function. On the first line of the implementation on the set function, it passed the key, from the key-value pair the was sent to it, into our custom hash function. If we scroll down to this hash function, we can see that it is a peculiar sight. The key is converted to a string (if it wasn’t already) and encoded explicitly into `utf-8`. Then you call the hexdigest() function on the md5 object which gives you the md5 hash string. Then again, you pass the string into the global function list() which converts the string into an array of separated values. Traversing over the array with the for loop, we convert each character value into its code point integer and accumulate that in k. This gives us an integer value that is unique to the key we passed in. But, this number is way bigger or smaller than our actual hashTableSize. So, mod it with the length of our hash table. The modulus operator gives you the remainder of the division operation. The remainder is always less than the value you divide by and this serves our purposes. 

```python
# @params {string} key
    # @returns {number}
    def hash(self, key):
        k = 0
        for s in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(s)
        return k % len(self.buckets)
```

Coming back to the set function, the keyHash now has a number that is in the range of 0 to the length of the hash table. As we want to use keys as a quick look up, we store the value of the keyHash in the keys dictionary with the key as the identifier. The keyHash is the index of where in the hash table the key-value pair will be stored hence the next line fetches the bucket from the hash table with the index keyHash and stores it in a new variable called bucketLinkedList.

Before we put anything in this bucket, which is actually a whole linked list, we need to make sure that the same key does not already exist in the linked list. If it exists, we need to update the key with the new value and if it doesn’t exist, we need to append the key-value pair to the end of our linked list. 

```python
# @param {string} key
    # @param {*} value
    def set(self, key, value):

        keyHash = self.hash(key)
        self.keys[key] = keyHash
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
        
        if node == None:
            bucketLinkedList.append({key: value})
        else:
            node.value[key] = value
```

The get and delete functions are pretty similar. You start off by using the hash to find which bucket the key-value pair is stored in. Once you get that linked list, you implement a custom linked list find which goes through the whole linked list and returns if it found your key. If it does you get your key-value pair and you can proceed to return or delete it. 

```python
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
```

The has function returns a true if there is a value if the key already exists inside the hash table. This can be implemented without the use of our keys dictionary and by writing custom linked list implementation as we did earlier. The keys from the keys dictionary are extracted in a list and we check if the key that the user wants to find is actually in it. If it is, return true else return false. The get keys extracts the keys from the keys dictionary is a list and just returns all of it.

```python
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
```


We hope you understood the power and also the imminent limitations and the hash table with this video. Please subscribe to the channel and like the video if you liked it or dislike the video if you didn’t. Consider supporting the channel if you want us to produce more content with the links in the description below. Thanks for watching and I will see you in the next video. Peace.



























