def isPalindrome(s):
    
    lp = 0
    rp = len(s)-1
    
    while True:
        
        
        
        while lp < len(s) and isValid(s[lp]) == False:
            lp +=1
            
            pass
        
        
        
        while rp > 0 and isValid(s[rp]) == False:
            rp -=1
            
        
        if rp >= len(s) or lp >= rp or lp >= len(s):
            return True
        
        
        left_val = s[lp]
        right_val = s[rp]
        
        if left_val.lower() != right_val.lower():
            return False
        lp +=1
        rp -=1
            
        
        
        
def isValid(letter):
    letter = ord(letter)
    if (letter >= ord("a") and letter <= ord("z")) or (letter >= ord("A") and letter <= ord("Z")) or (letter >= ord("0") and letter <= ord("9")):
        return True    
    else: 
        return False
    
    
print(isPalindrome(".,"))