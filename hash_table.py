class HashTable:
    def __init__(self,size):
        self.size =size
        self.table = [[] for _ in range(size)]

    def hash_fun(self,key):
        return key%self.size

    def get(self,key):
        index= self.hash_fun(key)
        bucket = self.table[index]

        for k,v in bucket:
            if k==key:
                return v
            
        return None

    def set(self,key,value):
        index = self.hash_fun(key)
        bucket = self.table[index]

        for i, (k,v) in enumerate(bucket):
            if k==key:
                bucket[i] = (key,value)
                return
            
        bucket.append((key,value))    
        

table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: hello
print(table.get(5251))  # Output: world
print(table.get(123))   # Output: good
print(table.get(22))    # Output: None (no value at 22 % 5 = 2)