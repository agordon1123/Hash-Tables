# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        def hash(key):
            total = 0
            for i in range(0, len(key)):
                key_ascii = ord(key[i])
                total += key_ascii
            
            return total % self.capacity
            # or
            # restucture to use _hash_mod
            # self._hash_mod(total)

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hashed_key = self._hash(key)

        if self.storage[hashed_key] == None:
            # create new LinkedPair
            self.storage[hashed_key] = LinkedPair(key, value)
        else:
            target = self.storage[hashed_key]

            while target is not None:
                if target.key == key:
                    # overwrite
                    target.value = value
                    return
                elif target.next == None:
                    # if at end, create new LinkedPair
                    target.next = LinkedPair(key, value)
                    return
                else:
                    # iterate
                    copy = target
                    target = copy.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)

        # if found at first element in LL
        if self.storage[hashed_key].key == key:
            copy = self.storage[hashed_key]
            del self.storage[hashed_key].key
            if copy.next:
                self.storage[hashed_key].next = copy.next
            else:
                self.storage[hashed_key] = None
            return
        
        else:
            # loop through and find
            target = self.storage[hashed_key]

            while target.next is not None:
                if target.next.key == key:
                    copy = target.next
                    del target.next
                    if copy.next:
                        target.next = copy.next
                        return
                    else:
                        target.next = None
                        return
                else:
                    # iterate
                    copy = target
                    target = copy.next
            
            return "Warning! Key not found!"
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)

        # this has multiple evaluations for the same thing
        if self.storage[hashed_key] == None:
            return None
        else:
            target = self.storage[hashed_key]
            if target.key == key:
                # if found at first element
                return self.storage[hashed_key].value
            else:
                # else loop through LL
                while target.next is not None:
                    if target.next.key == key:
                        return target.next.value
                    else:
                        # iterate
                        copy = target
                        target = copy.next
                
                return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create new HashTable with double the capacity
        copy = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        
        # copy over every element in range of old length
        for i in range(0, len(copy)):
            while copy[i] is not None:
                hashed_key = self._hash(copy[i].key)
                self.insert(copy[i].key, copy[i].value)
                self.storage[hashed_key].next = copy[i].next
                copy[i] = copy[i].next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
