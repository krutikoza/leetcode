def lengthOfLongestSubstring(s):
    hash_map = {}
    left_pointer = 0
    right_pointer = 0
    max_len = 1
    if len(s)==1:
        return 1
    if len(s)<1:
        return 0
    
    hash_map[s[0]] = 1
    while True:
        print(hash_map)
        right_pointer+=1
        if left_pointer > right_pointer:
            break
        if left_pointer > len(s)-1 or right_pointer > len(s)-1:
            break
        
        
        
        if s[right_pointer] in hash_map:
            while s[left_pointer] != s[right_pointer]:
                hash_map[s[left_pointer]] -= 1
                if hash_map[s[left_pointer]] == 0:
                    del hash_map[s[left_pointer]]
                left_pointer +=1
                
            left_pointer+=1
            
            
        else:
            if s[right_pointer] in hash_map:
                hash_map[s[right_pointer]] += 1
            else:
                hash_map[s[right_pointer]] = 1
            
        if len(hash_map) > max_len:
            max_len = len(hash_map)
            
            
    print(max_len)
            
            
lengthOfLongestSubstring("bbbbb")