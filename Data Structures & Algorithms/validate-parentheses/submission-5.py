class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "{([":
                stack.append(c)
            elif ((c in "})]" and len(stack) == 0) or (c == "}" and stack[-1] != "{") or (c == ")" and stack[-1] != "(") or (c == "]" and stack[-1] != "[")):
                return False
            else:
                stack.pop()
        return len(stack) == 0
