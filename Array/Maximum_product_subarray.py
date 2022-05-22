def maxProduct(nums):
    minimum = nums[0]
    maximum = nums[0]
    f_max = 1
    f_min = 1
    max_val = max(minimum,maximum)
    for i in range(1,len(nums),1):
        # if array value is positive
        if nums[i] >= 0:
            if maximum * nums[i] > nums[i]:
                f_max = maximum * nums[i]
            else:
                f_max = nums[i]
                
            if minimum * nums[i] < nums[i]:
                f_min = minimum * nums[i]
            else:
                f_min = nums[i]

        # if array value is negative
        else:
            if minimum * nums[i] > nums[i]:
                f_max = minimum * nums[i]
            else:
                f_max = nums[i]
                
            if maximum * nums[i] < nums[i]:
                f_min = maximum * nums[i]
            else:
                f_min = nums[i]
        
        maximum = f_max
        minimum = f_min
        
        max_val = max(max_val,maximum)
        max_val = max(minimum,max_val)
            
    return max_val
