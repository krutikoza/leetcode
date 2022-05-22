def search(nums, target):
    
    right_index_array = list(range(0,len(nums)))
    left_index_array = list(range(0,len(nums)))
    main_index = list(range(0,len(nums)))
    while True:
        print("main_index",main_index)
        print("nums",nums)
        if len(nums) <= 2:
            if len(nums) == 1:
                if nums[0] == target:
                    return main_index[0]
                else:
                    return -1
            else:
                if nums[0] == target:
                    return main_index[0]
                else:
                    if nums[1] == target:
                        return main_index[1]
                    else:
                        return -1
        mid = int(len(nums)/2)
        right_array = nums[mid::]
        left_array = nums[0:mid+1]
        
        right_index_array = main_index[mid::]
        left_index_array = main_index[0:mid+1]
        
        
        if (right_array[0] < target and (right_array[-1] >= target or right_array[-1] < right_array[0])) or (right_array[0] > target and (right_array[-1] >= target and right_array[-1] < right_array[0])):
            nums = right_array
            main_index = right_index_array
        else:
            nums = left_array
            main_index = left_index_array
            
            
            
x = search([1,2,3,4,0], 0)

print(x)