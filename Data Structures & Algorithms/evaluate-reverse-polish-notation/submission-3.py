class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for n in tokens:
            if n == "+":
                stack.append(stack.pop() + stack.pop())
            elif n == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif n == "*":
                stack.append(stack.pop() * stack.pop())
            elif n == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2 / v1))
            else:
                stack.append(int(n))

        return stack.pop()


