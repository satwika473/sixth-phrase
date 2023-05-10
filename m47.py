def kadane(arr):
    max_sum = float('-inf')
    curr_sum = 0
    
    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        curr_sum = max(curr_sum, 0)
    
    return max_sum
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum is", kadane(arr))
