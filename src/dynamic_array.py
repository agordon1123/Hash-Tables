class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0 # count is how much is currently used
        self.capacity = capacity # how much is currently allocated
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            # TODO: resize
            print("Error, array is full")
            return

        # shift everything to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)
    
    def splice(self, beginning_index, end_index): # default value
        # create subarray to store value
        sub_arr = []
        # copy beginning to end to subarray
        for i in range(beginning_index, end_index):
            sub_arr.append(self.storage[i])
        
        # opted to leave the original array alone
        # return subarray
        return sub_arr
