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
            # return self._hash_mod(total)

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
            # capture last element in LinkedList
            target = self.storage[hashed_key]
            
            if target.key == key:
                # overwrite
                target.value = value
                return
            elif target.next == None:
                # if at end, create new LinkedPair
                target.next = LinkedPair(key, value)
                return
            else:
                # loop through LL
                while target.next is not None:
                    if target.key == key:
                        # overwrite
                        target.value = value
                        return
                    elif target.next.key == key:
                        # check next element because of loop condition
                        target.next.value = value
                        return  
                    else:
                        # iterate
                        copy = target
                        target = copy.next
                # when at last element, set next as value being inserted
                if target.next == None:
                    target.next = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash(key)

        if key == "key-0":
            print("now")

        if self.storage[hashed_key].key == key:
            copy = self.storage[hashed_key]
            del self.storage[hashed_key].key
            if copy.next == None:
                self.storage[hashed_key] = None
            return
        else:
            # loop through and find
            target = self.storage[hashed_key]

            while target.next is not None:
                # may be able to only check the next key and cut this down

                # if target.key == key:
                #     # delete
                #     return

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

        if self.storage[hashed_key] == None:
            return None
        else:
            target = self.storage[hashed_key]
            if target.key == key:
                return self.storage[hashed_key].value
            else:
                # loop through LL
                while target.next is not None:
                    if target.key == key:
                        return target.value
                    # if last element has desired key
                    elif target.next.key == key:
                        return target.next.value
                    # keep moving
                    else:
                        copy = target
                        target = copy.next
                # self.storage[hashed_key] has values but none have desired key
                return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



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
