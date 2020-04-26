def isValid(self, s: str) -> bool:
    brackets = {')':'(', ']':'[', '}':'{'}
    stack = []
    for i in range(len(s)):
        if s[i] in brackets:
            if len(stack) == 0:
                return False
            if brackets[s[i]] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack) == 0:
        return True
    return False
