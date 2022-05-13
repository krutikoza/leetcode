def containsDuplicate(nums):
    val_dict = {}
    
    for i in range(len(nums)):
        if nums[i] in val_dict:
            return True
        
        val_dict[nums[i]] = i
        
    return False