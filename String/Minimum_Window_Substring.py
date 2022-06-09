# def minWindow(s, t):

#     if len(t) > len(s):
#         return ""
#     # Initialize the dictionary (one empty and one with required element)
#     countT, window = {}, {}
#     for i in t:
#         if i in countT:
#             countT[i] += 1
#         else:
#             countT[i] = 1
            

#     have, need = 0, len(countT)
#     result = 999999
#     res_pointer = []
#     lp = 0
    
#     for rp in range(len(s)):
        
#         if s[rp] in countT:
#             window[s[rp]] = 1 + window.get(s[rp], 0)

#             if window[s[rp]] == countT[s[rp]]:
#                 have += 1
            
        
#         print(window)
#         if have == need:
            
            
#             while have == need:
                
                
#                 if result > (rp - lp + 1):
#                     result = rp - lp + 1
#                     res_pointer = [lp,rp]
                
#                 if s[lp] in countT:
#                     window[s[lp]] -= 1
                
#                     if window[s[lp]] < countT[s[lp]]: 
#                         have -=1
                    
#                 lp +=1
                    
       
#     res_val = ""             
#     for i in range(res_pointer[0], res_pointer[1]+1):
#         res_val += s[i]
#     return res_val
            
        
# print(minWindow("a", "aa"))