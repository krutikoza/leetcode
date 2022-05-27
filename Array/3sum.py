def threeSum(nums):
    
    answer = []
    nums.sort()


    print(nums)    
    for i in range(len(nums)-2):
        left_pointer = i+1
        right_pointer = len(nums)-1
        target = nums[i]
        for j in range(i+1,len(nums),1):
            if i > 0 and nums[i] == nums[i-1]:
                break
            
            total_sum = target + nums[left_pointer] + nums[right_pointer]
            
            if total_sum < 0:
                left_pointer += 1
                
            elif total_sum > 0:
                right_pointer -= 1
            
            else:
                if left_pointer >= right_pointer:
                    break
                if len(answer) > 0 and (answer[-1][0] == target and answer[-1][2] == nums[right_pointer]):
                    left_pointer += 1
                    continue
                answer.append([target, nums[left_pointer], nums[right_pointer]])
                
                    
            
                
                
            

    return answer


print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))