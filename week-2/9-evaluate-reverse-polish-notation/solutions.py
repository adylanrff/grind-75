from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if token == "+":
                    stack.append(first_num+second_num)
                elif token == "-":
                    stack.append(first_num-second_num)
                elif token == "/":
                    stack.append(int(first_num / second_num))
                elif token == "*":
                    stack.append(first_num*second_num)

        return int(stack[0])
