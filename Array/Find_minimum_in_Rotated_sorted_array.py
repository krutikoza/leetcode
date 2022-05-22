def findMin(nums):
    nums_array = nums
    if len(nums) <=2:
        return min(nums)
    
    
    
    while True:
        
        
        mid = int( len(nums_array)/ 2 )
    
        left_array = nums_array[0:mid+1]
        right_array = nums_array[mid::]
        
    
    
        if len(nums_array) <=2:
            return min(nums_array)
        
        if right_array[0] > right_array[-1]:
            nums_array = right_array
            continue
    
        else:
            nums_array = left_array
            continue
        
        
        

    
ans = findMin([4,5,6,7,8,-2,-1])
print(ans)