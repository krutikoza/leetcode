def productExceptSelf(self, nums):
    pre = nums[0]
        
    answer = [1]*len(nums)


    for i in range(1,len(nums),1):
        answer[i] *= pre
        pre*= nums[i]
        
    print(answer)
    post = nums[-1]
    
    for i in range(len(nums)-2,-1,-1):
        answer[i] *= post
        post *= nums[i]

    return answer

      