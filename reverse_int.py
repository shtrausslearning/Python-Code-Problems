class Solution:
    
    def reverse(self, x: int) -> int: 
        neg = False
        if (x < 0):
            neg= True
            x = abs(x)

        n = 0 
        while (x != 0):
            left_digit =  x % 10 
            x = x // 10
            n = n * 10 + left_digit 

        if(neg):
            n *= -1
        
        if not ((-2**31) <= n <= (2**31 - 1)):
            return 0
        else:
            return n
