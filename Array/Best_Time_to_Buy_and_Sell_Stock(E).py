# time O(n)
# space O(1)

import sys

def maxProfit(prices):
    
    buy_pointer = 0
    sell_pointer = 1
    max_val = -sys.maxsize
    
    for i in range(len(prices)):
        
        if buy_pointer >= len(prices) or sell_pointer >= len(prices):
            if max_val < 0:
                return 0
            return max_val
        
        profit =  prices[sell_pointer] - prices[buy_pointer]
        
        if profit > max_val:
            max_val = profit
        
        
        
        if prices[sell_pointer] < prices[buy_pointer]:
            buy_pointer = sell_pointer
            sell_pointer += 1
        else:
            sell_pointer += 1
        
        
        
              
        
        

            