# Source: zyBooks: Figure 7.8.2: Hash table using chaining. W-1_ChainingHashTable_zyBooks_Key-Value.py
 
# Define the HashMap class.
class HashMap:
    
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=20):
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
      
    # Inserts a new item into the hash table.
    def insert(self, key, item): #  Does both insert and update 
        # Get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # Update key if it is already in the bucket
        for kv in bucket_list:
          if kv[0] == key:
            kv[1] = item
            return True
        
        # If not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
 
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # Get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # Search for the key in the bucket list
        for kv in bucket_list:
          if kv[0] == key:
            return kv[1]
        return None
 
    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # Get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # Remove the item from the bucket list if it is present.
        for kv in bucket_list:
          if kv[0] == key:
              bucket_list.remove([kv[0], kv[1]])