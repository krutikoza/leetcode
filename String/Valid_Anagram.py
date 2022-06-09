def isAnagram(s,t):
    
    s_string = {}
    t_string = {}
    
    
    for i in s:
        s_string[i] = 1 + s_string.get(i, 0)
        
    for i in t:
        t_string[i] = 1 + t_string.get(i, 0)
        
    if s_string == t_string:
        return True

    else: return False