def myAtoi(self, str: str) -> int:
        digits = '0123456789'
        sign = 1 #sign of number
        is_sign = 0 #number of signs in str
        started = False #is number has started
        ans = 0 #answer of program
        for char in str:
            if char not in digits and char not in ' -+' and not started: #if the first char is not sign, number or " " return 0
                return 0
            
            if char not in digits and is_sign >= 1 and not started: #if sign was caught and the next char is not number return 0
                return 0
                
            if char in digits: #if char of str is digit we'll count the number
                ans = ans * 10 + (ord(char) - 48)
                started = True
                #num += char   
            elif char not in digits and started: #if number ended we can go out of loop
                break
            
            if char == '-':
                sign = -1
                is_sign += 1
                
            if char == '+':
                is_sign += 1
            
            
        
        if ans * sign > 2**31 - 1:
            return 2**31 - 1
        if ans * sign < -2**31:
            return -2**31
            
        return ans * sign
