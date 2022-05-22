def maxSubArray(self, nums):
    max_val = -999999
    sum = 0
    
    for i in range(len(nums)):
        sum += nums[i]
        
        if max_val < sum:
            max_val = sum
            
        if sum < 0:
            sum = 0
            
    return max_val
                
            