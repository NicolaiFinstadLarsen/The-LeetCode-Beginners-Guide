class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # If the ransomNote is longer than magazine, we cannot make the ransomNote
        if len(ransomNote) > len(magazine):
            return False

        # Initialize a dictionary
        hash_set = {}
        for c in magazine:
            # Add a key : value pair with each letter of the magazine sample we have available
            # Increase the value with one 
            hash_set[c] = 1 + hash_set.get(c, 0)
            #print(hash_set)

        for c in ransomNote:
            if c not in hash_set or hash_set[c] <= 0:
                return False
            # Remove the value for the key [c] in ransomNote
            hash_set[c] -= 1
        
        return True


# I could use the Counter method from the Collections lib. But I dont know it well yet.
            
        