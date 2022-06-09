def characterReplacement(s, k):
    
    dict_list = {}
    lp = 0
    rp = -1
    max_val = 0
    while True:
        rp +=1
        if lp >= len(s) or rp >= len(s):
            return max_val
        
        if s[rp] in dict_list:
            dict_list[s[rp]] += 1    
        else:
            dict_list[s[rp]] = 1
            
         
         
        print(lp,rp)
        if sum(dict_list.values()) - max(dict_list.values()) <= k:
            
            if max_val < (rp)-(lp)+1:
                max_val = (rp)-(lp)+1
                
        
        else:
            while sum(dict_list.values()) - max(dict_list.values()) > k:
                dict_list[s[lp]] -=1
                lp +=1
                
                

    
        
        
        
print(characterReplacement("AABABBA",1))