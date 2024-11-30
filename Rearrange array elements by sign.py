def rearrange_by_sign(arr):
    # Separate positive and negative numbers into two lists
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    
    # Result array to store the rearranged elements
    result = []
    
    # Pointer for positive and negative arrays
    i, j = 0, 0
    
    # Alternate between positive and negative elements
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    
    # If there are remaining elements in pos or neg, append them
    result.extend(pos[i:])
    result.extend(neg[j:])
    
    return result

arr = [3, 1, -2, -5, 2, -4]
rearranged_arr = rearrange_by_sign(arr)
print(rearranged_arr)




def rearrange_by_sign(arr):
    # Create an array to store the rearranged elements
    result = [0] * len(arr) 
    # Initialize two pointers for positive and negative positions
    pos_index, neg_index = 0, 1
    
    for num in arr:
        if num > 0:
            result[pos_index] = num
            pos_index += 2
        else:
            result[neg_index] = num
            neg_index += 2
    
    return result

# Example usage
arr = [3, 1, -2, -5, 2, -4]
print(rearrange_by_sign(arr))