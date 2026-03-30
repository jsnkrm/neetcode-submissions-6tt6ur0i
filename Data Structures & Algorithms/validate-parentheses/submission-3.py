class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parMap = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in parMap:
                if stack and stack[-1] == parMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack .append(c)
        
        return True if not stack else False

