class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) > 0:
                    last_el = stack.pop()
                    if c == ")":
                        if last_el != "(":
                            return False
                    if c == "}":
                        if last_el != "{":
                            return False
                    if c == "]":
                        if last_el != "[":
                            return False
                else:
                    return False
                    
            
        return len(stack) == 0