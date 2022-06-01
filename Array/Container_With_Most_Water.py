def maxArea(height):
    max_water = -99
    len_height = len(height)-1
    front_pointer = 0
    back_pointer = len_height
    distance = len_height
    for i in range(len_height+1):
        if front_pointer >= back_pointer:
            return max_water
        volume = min(height[front_pointer], height[back_pointer]) * distance
        
        if volume > max_water:
            max_water = volume
            
            
        if height[front_pointer] < height[back_pointer]:
            front_pointer += 1
            distance -= 1
            
        else:
            back_pointer -= 1
            distance -= 1
            
            
print(maxArea([1,2,3,4,5]))