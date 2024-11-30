from typing import List

class Solution:
    def findDuplicates(self, arr: List[int], n: int) -> List[int]:
        # Initialize counts array with zeros
        counts = [0] * n
        
        # Count occurrences of each element
        for num in arr:
            counts[num] += 1
        
        # Collect elements that appear more than once
        duplicates = [i for i in range(n) if counts[i] > 1]
        
        # Return the sorted list of duplicates or [-1] if no duplicates
        return duplicates if duplicates else [-1]

if __name__== "__main__":
    obj = Solution()
    arr = [0, 3, 1, 2]  
    n = 4
    res = obj.findDuplicates(arr, n)  # Should return [-1] since no element is duplicated
    print(res)
