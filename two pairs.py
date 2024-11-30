class Solution:
    def getPairsCount(self, arr, sum):
        # Create an empty dictionary to store the frequency of elements
        freq = {}
        count = 0
        # Iterate through the array
        for num in arr:
            # Calculate the difference needed to reach the target sum
            diff = sum - num
            
            # If the difference is already in the dictionary, we found a pair
            if diff in freq:
                count += freq[diff]
            
            # Update the frequency of the current number in the dictionary
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        return count

# Example usage:
arr = [1, 2, 5, 4]
sum = 6
s = Solution()
res = s.getPairsCount(arr, sum)
print("Total pairs:",res)