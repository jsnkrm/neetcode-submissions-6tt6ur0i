class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        digits = ["0","1","2","3","4","5","6","7","8","9"]

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                first, second = stack.pop(), stack.pop()
                ans = second - first
                stack.append(ans)
            elif c == "*":
                first, second = stack.pop(), stack.pop()
                ans = first * second
                stack.append(ans)
            elif c == "/":
                first, second = stack.pop(), stack.pop()
                ans = int(second / first)
                stack.append(ans)
            else:
                stack.append(int(c))
            
        return stack.pop()
