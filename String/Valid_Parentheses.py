def isValid(s):
        
    ref_dictionary = {"}":"{","]":"[",")":"("}

    stack = []
    for i in range(len(s)):
        if s[i] in ref_dictionary.keys():
            if i == 0:
                return False
            
            
            if stack != [] and stack[-1] == ref_dictionary[s[i]]:
                stack.pop(-1)
                
            else:
                return False
            
        else:
            stack.append(s[i])
            
    if stack == []:
        return True
    
    else: 
        return False
        
print(isValid("()[][[][]]]{}"))