import numpy as np


class dicti:
    def __init__(self, expected_size):
        self.inner_array = []
        for _ in range(0,expected_size):
            self.inner_array.append([])
        
        self.size = expected_size

    def get(self, key):
        index = self.hash(ord(key))
        value_vec = self.inner_array[index]
        for (ikey, value) in value_vec:
            if ikey == key:
                return value
        return -1     
    
    def set(self, key, value):
        index = self.hash(ord(key))
        value_vec = self.inner_array[index]
        for (ikey, value) in value_vec:
            if ikey == key:
                return 
        value_vec.append((key, value))    
    
    def hash(self, key: int):
        index = key % self.size
        return index
