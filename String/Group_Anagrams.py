def groupAnagrams(strs):
    dictionary = {}
            
    for i in range(len(strs)):
        char_arr = [0]*26    
        for j in range(len(strs[i])):
            char_arr[ord(strs[i][j]) - ord("a")] += 1
        
        if str(char_arr) in dictionary.keys():
            dictionary[str(char_arr)].append(strs[i])
        else:
            dictionary[str(char_arr)] = [strs[i]]
            
    return dictionary.values()

