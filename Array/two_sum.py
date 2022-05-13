# time O(n)
# space O(n^2)

def twoSum(nums,target):
    difference_dict = {}
    
    for i in range(len(nums)):
        difference = target-nums[i]
        
        if difference in difference_dict:
            return [i, difference_dict[difference]]
        
        difference_dict[nums[i]] = i
        